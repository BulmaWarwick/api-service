import os
import json
from typing import Any, Dict, Optional, List
from datetime import datetime

def read_json_file(file_path: str) -> Dict[str, Any]:
    """Read and parse a JSON file."""
    with open(file_path, 'r') as f:
        return json.load(f)

def write_json_file(file_path: str, data: Dict[str, Any]) -> None:
    """Write data to a JSON file."""
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

def ensure_directory_exists(dir_path: str) -> None:
    """Create a directory if it doesn't exist."""
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def get_timestamp_string() -> str:
    """Return current timestamp as a string."""
    return datetime.now().isoformat()

def filter_dict(data: Dict[str, Any], keys: List[str]) -> Dict[str, Any]:
    """Filter a dictionary to only include specified keys."""
    return {k: v for k, v in data.items() if k in keys}

def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Merge two dictionaries, with dict2 taking precedence."""
    return {**dict1, **dict2}

def validate_email(email: str) -> bool:
    """Validate an email address format."""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def get_env_variable(key: str, default: Optional[str] = None) -> Optional[str]:
    """Get an environment variable or return a default value."""
    return os.getenv(key, default)