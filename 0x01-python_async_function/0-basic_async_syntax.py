#!/usr/bin/env python3
""" Module that cintains a async fumctuon that delays fo a random second
function and returns the random secind"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Args:
            max_delay- The upper range of the random delay float
        Return:
            The random float in second
    """
    random_float = random.uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float
