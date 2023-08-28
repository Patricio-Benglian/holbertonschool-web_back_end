#!/usr/bin/env python3
'''
6-sum_mixed_list module
'''
from typing import List, Union
import typing


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Returns sum of list of floats and ints"""
    output: float = 0
    for value in mxd_list:
        output += value
    return output
