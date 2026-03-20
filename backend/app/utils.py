"""
Shared utility helpers.
"""
import re


def clean_json_str(raw: str) -> str:
    """
    Strip accidental markdown fences from an LLM JSON response.
    lstrip/rstrip strip individual characters, NOT substrings —
    so we use a proper regex instead.
    """
    return re.sub(r'^```(?:json)?\s*|\s*```$', '', raw.strip()).strip()
