#!/usr/bin/env python3
'''
Takes a string and int or float and returns a tuple containing
the string and the square of the int or float
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    Takes a string and int or float and returns a tuple containing
    the string and the square of the int or float
    '''
    return (k, v**2)
