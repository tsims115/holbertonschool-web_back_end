#!/usr/bin/env python3
"""Simple Pagination"""
import csv
import math
from typing import List, Tuple, Dict, Union, Optional


def index_range(page: int, page_size: int) -> Tuple[int]:
    """index range of pages top return"""
    return (((page - 1) * page_size), ((page - 1) * page_size) + page_size)


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
        """Get page from self.__dataset"""
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        rang = index_range(page, page_size)
        return self.dataset()[rang[0]: rang[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Union[int, List[str]]]:
        """Returns a dictionary"""
        rows = self.get_page(page, page_size)
        next_page = page + 1
        prev_page = page - 1
        if self.get_page(page + 1, page_size) == []:
            next_page = None
        if self.get_page(page - 1, page_size) == [] or prev_page <= 0:
            next_page = None
        return {
            'page_size': len(rows),
            'page': page,
            'data': rows,
            'next_page': next_page,
            'prev_page': page - 1,
            'total_pages': math.ceil(len(self.dataset()) / page_size)
        }
