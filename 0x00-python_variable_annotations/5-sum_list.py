#!/usr/bin/env python3
"""module containing type annotated function that returns sum of input"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """type annoted function that return sum ofinput list elements"""
    return sum(input_list)
