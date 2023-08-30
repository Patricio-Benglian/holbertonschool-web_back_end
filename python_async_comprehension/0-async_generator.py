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
    """test"""
    executions = [randgen(), randgen(), randgen(), randgen(), randgen(),
                  randgen(), randgen(), randgen(), randgen(), randgen()]
    for yielded_num in asyncio.as_completed(executions):
        yield await yielded_num
