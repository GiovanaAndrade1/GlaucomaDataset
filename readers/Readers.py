import os
from pathlib import Path

import numpy as np
from PIL import Image

from config.Settings import SUPPORTED_EXTENSIONS


class PillowImageReader:
    def read(self, path: Path) -> np.ndarray:
        return np.array(Image.open(path))


class GlaucomaBenchmarkReader:

    def __init__(self, artery_folder: Path, vein_folder: Path) -> None:
        self._artery_folder = Path(artery_folder)
        self._vein_folder   = Path(vein_folder)

    def load_pairs(self) -> dict[str, dict[str, Path]]:
        pairs = {}

        for path in self._iter_images(self._artery_folder):
            pairs[path.stem] = {"artery": path, "vein": self._vein_folder / path.name}
            
        return pairs

    @staticmethod
    def _iter_images(folder: Path):
        for entry in os.scandir(folder):
            if Path(entry.path).suffix.lower() in SUPPORTED_EXTENSIONS:
                yield Path(entry.path)