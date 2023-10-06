#!/usr/bin/env python3
"""This module provides a function that returns tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return tuple conatianing the first and second  args"""
    return (k, v*v)
