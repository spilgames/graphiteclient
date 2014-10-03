import requests


class GraphiteClient(object):
    def __init__(self, base_url):
        self.base_url = base_url

    def run(self, query):
        # TODO: Raise exception on invalid result
        print 'Query: ', query
        url = self.base_url + '/render?' + query
        print 'Url: ', url
        ret = requests.get(url, verify=False)
        print ret
        return ret.json()