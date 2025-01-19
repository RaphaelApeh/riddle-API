import json
from pathlib import Path
from functools import lru_cache

from django.conf import settings

DATA_DIR = settings.BASE_DIR / "data" 

@lru_cache()
def load_data(path: Path | None=DATA_DIR):
    
    for json_file in path.glob("*.json"):
        if not json_file.exists():
            raise ImportError("This path does not exists.")
        
        with open(json_file, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data