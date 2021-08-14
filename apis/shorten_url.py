"""This API will shorten the given input url"""

import json
import datetime
from requests.models import PreparedRequest
import requests.exceptions
import uuid
import falcon


from dal.dbconnection import session_scope
from dal import dbconnection, dal
from config import CURRENT_CONFIG as config
import utils
from cache import Cache


class ShortenUrl:

    def __init__(self, lambda_context=None):
        self.lambda_context = lambda_context
        self.dal = None
        self.log = None

    def on_post(self, req, resp):

        req_body = req.bounded_stream.read()

        validated_req_body = self.validate_params(req_body)
        if type(validated_req_body) is str:
            resp.body = json.dumps({'message': validated_req_body, 'data': {}})
            resp.status = falcon.HTTP_400
            return

        # Create a db session
        with session_scope() as session:
            self.dal = dal.DAL(session, self.log)

        # check if url already shortened in Cache
        existing_data = Cache.get_url(validated_req_body['link'])
        if existing_data is not None:
            print('Data served from cache')
            already_existing = True
            short_url = f"{config['SHORTENED_BASE_URL']}{existing_data}"
        else:
            # check in db
            print('Data served from db')
            existing_data, already_existing = self.dal.get_url(validated_req_body['link'])
            if existing_data:
                short_url = f"{config['SHORTENED_BASE_URL']}{existing_data[0].uid}"
                Cache.set_url(existing_data[0].uid, existing_data[0].link)
            else:
                already_existing = False

        # create a new short url
        if not already_existing:
            status, short_url = self.shorten_url(validated_req_body)
            self.dal.close_session()
        else:
            status = True
        # creating response
        if status:
            resp.body = json.dumps({'data': {'link': short_url}, 'message': 'success'})
            resp.status = falcon.HTTP_200
        else:
            resp.status = falcon.HTTP_500

    @staticmethod
    def validate_params(params):
        required_params = {'link': str}
        try:
            params = json.loads(params)
        except:
            return "Input should be a json"
        required_params = utils.check_if_param_exists(params, required_params)
        if type(required_params) is str:
            return required_params

        # validate url
        prepared_request = PreparedRequest()
        try:
            prepared_request.prepare_url(params['link'], None)
            if not params['link'].startswith('https'):
                raise Exception('Invalid URL')
        except Exception as e:
            return 'input url is invalid. Please provide a valid url'

        return required_params

    def shorten_url(self, validated_req_body):
        uid = str(uuid.uuid4())[:5]
        status = self.dal.insert_url(uid, validated_req_body['link'])
        short_url = f"{config['SHORTENED_BASE_URL']}{uid}"
        Cache.set_url(uid, short_url)
        return status, short_url
