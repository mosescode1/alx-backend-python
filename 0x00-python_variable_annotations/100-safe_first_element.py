#!/usr/bin/env python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""

from typing import Any, Union, Sequence, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Union[Sequence[Any]], None]:
  """"sumary_line"""

    if lst:
        return lst[0]
    else:
        return None
