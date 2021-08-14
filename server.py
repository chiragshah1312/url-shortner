"""Create server and attach the APIs"""

import falcon
from wsgiref.simple_server import make_server

import urls
from apis.shorten_url import ShortenUrl

from dal import dbconnection
import config


def start_server():
    api = falcon.API()
    dbconnection.DBSession.initdsn(config.CURRENT_CONFIG['DB_CONN'])

    api.add_route(urls.SHORTEN_URL, ShortenUrl())

    return api


api = start_server()


if __name__ == "__main__":
    with make_server('0.0.0.0', 8000, start_server()) as httpd:
        print('Serving on port 8000...')
        httpd.serve_forever()
