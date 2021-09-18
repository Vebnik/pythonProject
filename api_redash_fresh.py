import requests
import time
from pprint import pprint
import json


class RedashApi:

    def __init__(self, api_key):
        self.api_key = api_key

    def poll_job(self, s, redash_url, job):
        # TODO: add timeout
        while job['status'] not in (3, 4):
            response = s.get('{}/api/jobs/{}'.format(redash_url, job['id']))
            job = response.json()['job']
            time.sleep(1)

        if job['status'] == 3:
            return job['query_result_id']

        return None


    def get_fresh_query_result(self, redash_url, query_id, api_key, params):
        s = requests.Session()
        s.headers.update({'Authorization': 'Key {}'.format(api_key)})

        payload = dict(max_age=0, parameters=params)

        response = s.post('{}/api/queries/{}/results'.format(redash_url, query_id), data=json.dumps(payload))

        if response.status_code != 200:
            pprint('{}/api/queries/{}/results'.format(redash_url, query_id))
            pprint(response.__dict__)
            pprint(payload)
            raise Exception('Refresh failed.')

        result_id = self.poll_job(s, redash_url, response.json()['job'])

        if result_id:
            response = s.get('{}/api/queries/{}/results/{}.json'.format(redash_url, query_id, result_id))
            if response.status_code != 200:
                raise Exception('Failed getting results.')
        else:
            raise Exception('Query execution failed.')

        return response.json()['query_result']['data']['rows']


    def get_query_result(self, query_id, params):
        return self.get_fresh_query_result('https://app.redash.io/skyeng', query_id, self.api_key, params)