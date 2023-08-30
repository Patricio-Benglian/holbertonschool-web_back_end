#!/usr/bin/env python3
'''
0-async_generator module
'''
import asyncio
from random import uniform
from typing import Generator


async def randgen() -> float:
    """generates float from 0-10"""
    await asyncio.sleep(1)
    return uniform(0, 10)


async def async_generator() -> Generator[float, None, None]:
    """Yields 10 values between 0 and 10"""
    executions = [randgen(), randgen(), randgen(), randgen(), randgen(),
                  randgen(), randgen(), randgen(), randgen(), randgen()]
    # as_completed is like gather in that it executes synchronously i think
    for yielded_num in asyncio.as_completed(executions):
        yield await yielded_num
