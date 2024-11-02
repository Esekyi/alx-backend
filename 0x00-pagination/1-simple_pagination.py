#!/usr/bin/env python3
"""Simple helper function"""
from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of size two, with a start
    and end index.
    """

    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialize the class
                """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a page with the given page number and page size"""
        assert isinstance(page, int) and isinstance(
            page_size, int) and page > 0 and page_size > 0
        self.dataset()
        indexes = index_range(page, page_size)
        if indexes[0] >= len(self.__dataset):
            return []
        return self.__dataset[indexes[0]:indexes[1]]
