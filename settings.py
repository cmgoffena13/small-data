from dotenv import load_dotenv
from pathlib import Path
import os


path = Path(".").resolve()

load_dotenv(path)

DATA_WAREHOUSE_URL = os.environ["DATA_WAREHOUSE_URL"]