#!/usr/bin/env python3
"""Simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of size two, with a start
    and end index.
    """

    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
