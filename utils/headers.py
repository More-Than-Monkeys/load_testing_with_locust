from __future__ import annotations
from typing import Dict

def build_base_headers() -> Dict[str, str]:
    """Return default headers for all requests."""
    return {
        "User-Agent": "locust-sample",
        "Accept": "text/html",
    }
