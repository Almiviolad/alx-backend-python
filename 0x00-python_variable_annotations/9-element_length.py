#!/usr/bin/env python3
"""module.for function that returns length of elemnt in param"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """retuns tuple of elment and lenngth of elements in list"""
    return [(i, len(i)) for i in lst]
