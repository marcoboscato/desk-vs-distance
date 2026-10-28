from pathlib import Path

# __file__ è il percorso di questo file (config.py)
# .parent prende la cartella che lo contiene (la root ADAMS)
ROOT_DIR = Path(__file__).resolve().parent

# Percorsi delle sottocartelle principali
DATA_DIR = ROOT_DIR / "data"