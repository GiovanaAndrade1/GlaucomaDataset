from pathlib import Path

DATASET_ROOT = Path( r"C:\Usuários\02103593669\Documents\GlaucomaDataset" )
ARTERY_FOLDER_NAME = "vessel-artery"
VEIN_FOLDER_NAME   = "vessel-vein"


OUTPUT_DIR      = Path("vessel_Analysis/output")
CSV_FILENAME    = "vessel_analysis_results.csv"
REPORT_FILENAME = "vessel_analysis_report.txt"


SUPPORTED_EXTENSIONS = {".png", ".jpg", ".jpeg"}


GLAUCOMA_DISCREPANCY_THRESHOLD_PCT: float | None = None