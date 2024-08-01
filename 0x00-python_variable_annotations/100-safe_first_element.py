#!/usr/bin/env python3
from typing import Any, Union, Sequence, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Union[Sequence[Any]], None]:
    if lst:
        return lst[0]
    else:
        return None
