#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """method with two integer arguments"""
        assert isinstance(index, int) and index > 0
        assert isinstance(page_size, int) and page_size > 0
        ind = self.__indexed_dataset
        if ind is None:
            ind = 0
        if index >= len(ind):
            return {'index': index, 'data': [], 'page_size': 0,
                    'next_index': None}
        start = index
        end = start + page_size
        data = [ind[i] for i in range(start, end) if i in ind]
        next_index = end if end < len(ind) else None
        return {'index': index, 'data': data, 'page_size': page_size,
                'next_index': next_index}
