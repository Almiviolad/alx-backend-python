#!/usr/bin/env python3
"""This module.contains.fumction that gets key if its in dict"""
from typing import Mapping, Any, Optional, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Optional[T] = None) -> Union[Any, T]:
    """returns value belonging to key in dict"""
    if key in dct:
        return dct[key]
    else:
        return default
