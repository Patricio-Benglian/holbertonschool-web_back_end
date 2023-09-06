#!/usr/bin/env python3
"""
simple pagination
"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns start index and end index"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


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
        """gets page of dataset"""
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        start_index, end_index = index_range(page, page_size)
        return self.dataset()[start_index: end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """returns dict with many values pertaining to dataset"""
        output = {}
        # These two are self evident
        output["page_size"] = page_size
        output["page"] = page
        # The actual data to be shown
        output["data"] = self.get_page(page, page_size)
        # next, previous, and total amount of pages
        # (21 % 5 > 0) resolves to True (aka 1), thus rounds up if not even
        total_pages = -(-len(self.dataset()) // page_size)
        output["next_page"] = page + 1 if page < total_pages else None
        output["prev_page"] = page - 1 if page > total_pages else None
        output["total_pages"] = total_pages
        return output
