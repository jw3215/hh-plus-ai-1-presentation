from typing import Callable, TypeVar, Generic, Any
import inspect

_T = TypeVar("_T")
_R = TypeVar("_R")


class Pipe(Generic[_T, _R]):
    def __init__(self, function: Callable[[_T], _R]):
        self.function = function

    def __ror__(self, other: _T) -> _R:
        return self.function(other)

    def __call__(self, x: _T) -> _R:
        return self.function(x)


def pipe_decorator(f: Callable[[_T], _R]) -> Pipe[_T, _R]:
    sig = inspect.signature(f)
    params = sig.parameters
    if len(params) != 1:
        raise ValueError("Function must have exactly one parameter")
    return Pipe(f)