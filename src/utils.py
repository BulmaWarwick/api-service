# utils.py

import os
import json
from datetime import datetime, timedelta
from typing import List, Dict

def load_config() -> Dict:
    with open('config.json') as f:
        config = json.load(f)
    return config

def get_abs_path(rel_path: str) -> str:
    return os.path.join(os.path.dirname(__file__), rel_path)

def is_valid_date(date_str: str) -> bool:
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def get_date_range(start_date: str, end_date: str) -> List[str]:
    date_range = []
    start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
    end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
    while start_date_obj <= end_date_obj:
        date_range.append(start_date_obj.strftime('%Y-%m-%d'))
        start_date_obj += timedelta(days=1)
    return date_range