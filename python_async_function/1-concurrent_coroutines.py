#!/usr/bin/env python3
'''
1-concurrent_coroutines module
'''
import typing


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """returns list of length n with delays up to max_delay"""
    list_times = []
    for i in range(n):
        list_times.append(await wait_random(max_delay))
    return list_times
