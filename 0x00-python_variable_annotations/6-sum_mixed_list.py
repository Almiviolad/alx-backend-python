#!/usr/bin/env python3
"""This module contains function that retisns sum of a list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns tge sum of theelement in the mixed arry parameter"""
    return sum(mxd_lst)
