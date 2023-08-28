#!/usr/bin/env python3
'''
5-sum_list module
'''
import typing


def sum_list(input_list: typing.List[float]) -> float:
    """adds list of floats"""
    output: float = 0
    for value in input_list:
        output += value
    return output
