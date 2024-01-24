#!/usr/bin/env python3
""" cache and tracker script"""
import redis
import requests
from typing import Callable
from functools import wraps


r = redis.Redis()


def count_access(method: Callable) -> Callable:
    """ counting how many time the page have being accessed"""
    @wraps(method)
    def wrapper(url):
        """wrapper method"""
        r.incr(f"count:{url}")

        html_value = r.get(f"cache:{url}")
        if html_value:
            return html_value.decode("utf-8")
        response_html = method(url)
        r.psetex(f"cache:{url}", 10000, response_html)
        return response_html
    return wrapper


@count_access
def get_page(url: str) -> str:
    """ getting the html from the url """

    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    get_page("http://slowwly.robertomurray.co.uk")
