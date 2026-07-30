from typing import Callable
from functools import partial

def suppress(f: Callable, ignore: tuple) -> Callable:
    