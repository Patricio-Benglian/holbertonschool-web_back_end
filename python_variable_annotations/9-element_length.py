#!/usr/bin/env python3
'''
9-element_length module
'''
from typing import Iterable, List, Sequence, Tuple
import typing


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns list of tuples with original value and its length"""
    return [(i, len(i)) for i in lst]
