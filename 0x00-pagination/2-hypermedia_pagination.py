#!/usr/bin/env python3
"""get_hyper method that takes the same arguments"""


import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> int:
    """index_range that takes two integer arguments page and page_size"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
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
            assert isinstance(page, int) and page > 0
            assert isinstance(page_size, int) and page_size > 0
            start, end = index_range(page, page_size)
            dataset = self.dataset()
            if start >= len(dataset):
                return ([])
            return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """get_hyper method that takes the same arguments"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        dataset = self.dataset()
        page_size = len(dataset[start:end])
        data = dataset[start:end]
        if page_size <= 0:
            total = math.ceil(len(dataset) / page)
        total = math.ceil(len(dataset) / page_size)
        next_page = page + 1 if page < total else None
        prev_page = page - 1 if page > 1 else None
        total_pages = total
        return {'page_size': page_size, 'page': page, 'data': data,
                'next_page': next_page,
                'prev_page': prev_page, 'total_pages': total}
