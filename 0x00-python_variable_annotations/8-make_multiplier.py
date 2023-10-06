#!/usr/bin/env python3
"""This module.is for fuction that multiply param float and another floaf"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ a float multiplier fuction maker"""
    def multiply(n: float) -> float:
        """multiplies two.floats"""
        return n * multiplier
    return multiply
