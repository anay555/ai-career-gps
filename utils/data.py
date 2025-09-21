import os
import json
from typing import Any, Dict, List, Optional

import requests

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data", "processed")


def _read_local_json(filename: str) -> Optional[Any]:
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _get_json(url: str, timeout: int = 8) -> Optional[Any]:
    try:
        resp = requests.get(url, timeout=timeout)
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return None


def get_streams_data(api_url: Optional[str]) -> List[Dict[str, Any]]:
    # Prefer API if available
    if api_url:
        data = _get_json(f"{api_url.rstrip('/')}/api/streams")
        if isinstance(data, list):
            return data
    # Fall back to local
    data = _read_local_json("streams.json")
    return data if isinstance(data, list) else []


def get_colleges_data(api_url: Optional[str]) -> List[Dict[str, Any]]:
    if api_url:
        data = _get_json(f"{api_url.rstrip('/')}/api/colleges")
        if isinstance(data, list):
            return data
    data = _read_local_json("colleges.json")
    return data if isinstance(data, list) else []


def get_skills_data(api_url: Optional[str], role: Optional[str] = None) -> List[Dict[str, Any]]:
    if api_url:
        url = f"{api_url.rstrip('/')}/api/skills/recommendations"
        if role:
            url += f"?role={role}"
        data = _get_json(url)
        if isinstance(data, list):
            return data
    data = _read_local_json("skills.json")
    return data if isinstance(data, list) else []
