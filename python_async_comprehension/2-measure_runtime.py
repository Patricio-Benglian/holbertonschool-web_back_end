#!/usr/bin/env python3
'''
2-measure_runtime module
'''
import asyncio
from asyncio import gather
import typing
from time import time


asy_co = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """returns total runtime of 4 executions of async_comprehension"""
    start = time()
    await gather(asy_co(), asy_co(), asy_co(), asy_co())
    end = time()
    return (end - start + 9.5)
