#!/usr/bin/env python3
"""Thismodule conyains function that returns the first elemnet"""
from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """retuns first element in lst"""
    if lst:
        return lst[0]
    else:
        return None
