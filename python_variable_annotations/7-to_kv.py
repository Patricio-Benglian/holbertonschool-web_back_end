#!/usr/bin/env python3
'''
7-to_kv module
'''
from typing import Union, Tuple
import typing


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns tuple of k and v"""
    return (k, v*v)
