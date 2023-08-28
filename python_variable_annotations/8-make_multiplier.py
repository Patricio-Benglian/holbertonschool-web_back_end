#!/usr/bin/env python3
'''
8-make_multiplier module
'''
from typing import Callable
import typing


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns function that multiplies num by multiplier"""
    def mult_func(num: float) -> float:
        """returns number * multiplier"""
        return multiplier * num
    return mult_func
