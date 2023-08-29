#!/usr/bin/env python3
'''
2-measure_runtime module
'''
import typing
from asyncio import run
from time import time


wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures average time elapsed"""
    start = time()
    run(wait_n(n, max_delay))
    end = time()
    elapsed_time = end - start
    return elapsed_time / n
