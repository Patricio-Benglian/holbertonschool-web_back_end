#!/usr/bin/env python3
'''
3-tasks module
'''
import asyncio
import typing

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """returns asyncio Task"""
    return asyncio.create_task(wait_random(max_delay))