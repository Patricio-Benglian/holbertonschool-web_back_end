#!/usr/bin/env python3
'''
0-basic_async_syntax module
'''
import asyncio
from random import uniform


async def wait_random(max_delay=10):
    """waits random delay between 0 and max_delay"""
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
