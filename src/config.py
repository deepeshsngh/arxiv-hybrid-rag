from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw" / "arxiv-metadata-oai-snapshot.json"
PROCESSED = ROOT / "data" / "processed"
EMB_DIR = ROOT / "embeddings"
INDEX_DIR = ROOT / "indexes"