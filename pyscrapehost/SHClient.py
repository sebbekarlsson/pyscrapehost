import requests
import json


class SHClient(object):
    def __init__(self, host, token):
        self.host = host
        self.token = token
        self.baseurl = '{}/api'.format(self.host.rstrip('/'))
        self.sess = requests.Session()

    def make_request(self, endpoint, kvargs=None):
        data = {
                'token': self.token
                }
        if kvargs:
            for k, v in kvargs:
                data[k] = v
        
        print(self.baseurl + endpoint)
        return self.sess.post(self.baseurl + endpoint, data=json.dumps(data))

    def get_scrapers(self):
        endpoint = '/scrapers'
        result = self.make_request(endpoint)
        
        return json.loads(result.text)

    def get_scraper_matches(self, scraper_id, offset=0):
        endpoint = '/scraper/{scraper_id}/matches/{offset}'
        result = self.make_request(
                endpoint.format(
                    scraper_id=scraper_id,
                    offset=offset
                    )
                )

        return json.loads(result.text)
