import requests


class GraphiteClient(object):
    def __init__(self, base_url):
        self.base_url = base_url

    def run(self, query):
        url = self.base_url + '/render?' + query
        ret = requests.get(url, verify=False)
        ret.raise_for_status()
        return ret.json()
