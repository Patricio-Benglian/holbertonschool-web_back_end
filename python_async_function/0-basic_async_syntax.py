#!/usr/bin/env python3
'''
0-basic_async_syntax module
'''
import asyncio
from random import uniform
import typing


async def wait_random(max_delay: int=10) -> float:
    """waits random delay between 0 and max_delay"""
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
