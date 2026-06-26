import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from readers.Readers     import GlaucomaBenchmarkReader
from analyzers.vessel_Analysis import VesselPairAnalyzer