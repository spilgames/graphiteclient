import requests


class GraphiteClient(object):
    def __init__(self, base_url):
        self.base_url = base_url

    def run(self, query):
        # TODO: Raise exception on invalid result
        url = self.base_url + '/render?' + query
        ret = requests.get(url, verify=False)
        return ret.json()
