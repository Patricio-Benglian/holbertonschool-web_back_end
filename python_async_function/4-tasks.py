#!/usr/bin/env python3
'''
4-tasks module
'''
import typing


wait_random = __import__("0-basic_async_syntax").wait_random
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """returns list of length n with delays up to max_delay"""
    list_times = []
    for i in range(n):
        list_times.append(await task_wait_random(max_delay))
    return sorted(list_times)
