"""This class will act as our cache to store the original & shortened url """

import sys


class Cache:
    __urls = {}

    @classmethod
    def get_url(cls, link):
        return cls.__urls.get(link, None)

    @classmethod
    def set_url(cls, uid, link):
        # if cache grows more than 5MB then clear it
        if sys.getsizeof(cls.__urls) >= 5000000:
            cls.__urls = {}

        cls.__urls[link] = uid
