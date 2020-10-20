#!/usr/bin/env python3
'''
Returns a function that multiplies a float by a multiplier (itself)
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Returns a function that multiplies a float by a multiplier (itself)
    '''
    return lambda x: x * multiplier
