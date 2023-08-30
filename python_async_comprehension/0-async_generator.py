#!/usr/bin/env python3
'''
0-async_generator module
'''
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """waits 1 second then yields random number between 0 and 10"""
    for iter in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
