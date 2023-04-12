from __future__ import annotations
from typing import Union

class ClosedRange():
    def __init__(self,lower_limit,upper_limit) -> None:
        if lower_limit > upper_limit:
            raise ValueError
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit

    def __str__(self) -> str:
        return f"[{self.lower_limit},{self.upper_limit}]"

    def is_included(self, arg:Union[int, ClosedRange]) -> bool:
        if isinstance(arg, int):
            return self.lower_limit <= arg <= self.upper_limit
        else:
            return self.lower_limit <= arg.lower_limit and arg.upper_limit <= self.upper_limit

    def __eq__(self, __value:ClosedRange) -> bool:
        return __value.upper_limit == self.upper_limit and __value.lower_limit == self.lower_limit