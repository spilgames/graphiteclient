from client import GraphiteClient
from result import GraphiteResultSet


class GraphiteQueryTarget(object):
    '''Represents a single graphite target (target=<something>'''

    def __init__(self, query, name=None, color=None):
        self.query = query
        self.name = name
        self.color = color

    def __unicode__(self):
        querytext = self.query
        if self.name:
            querytext = 'alias({0}, "{1}")'.format(querytext, self.name)

        return '{0}'.format(querytext)


class GraphiteQuery(object):
    attrs = {}
    targets = []
    zero_missing = False

    def __init__(self, client=None, base_url=None, zero_missing=False, **kwargs):
        if not client:
            self.client = GraphiteClient(base_url)
        else:
            self.client = client

        self.zero_missing = zero_missing
        self.attrs.update(kwargs)

    def build_query(self):
        '''Builds query string'''
        querystring = []
        querystring.extend([('target', unicode(x)) for x in self.targets])
        querystring.extend([(k, v) for k, v in self.attrs.iteritems()])
        return '&'.join('{0}={1}'.format(x[0], x[1]) for x in querystring)

    def add_target(self, *args, **kwargs):
        self.targets.append(GraphiteQueryTarget(*args, **kwargs))

    def run(self):
        self.attrs['format'] = 'json'
        self.result = GraphiteResultSet(self.client.run(self.build_query()), self)
        return self.result

