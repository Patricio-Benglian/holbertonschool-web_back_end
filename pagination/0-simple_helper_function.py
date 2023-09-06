#!/usr/bin/env python3
"""
simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns start index and end index"""
    # page_size is indexes per page
    # page is which page of the list we care
    # page * page_size gives the final index in the page we want
    # (page - 1) * page_size should thus give the final index of the page
    # before the one we want
    # (the wording was confusing so i explain here xd)
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
