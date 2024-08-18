#!/usr/bin/env python3
"""index_range that takes two integer arguments page and page_size""" 


def index_range(page, page_size):
    """index_range that takes two integer arguments page and page_size"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
