class GraphiteResult(object):
    '''Represents individual result'''

    def __init__(self, result, zero_missing):
        self.target = result['target']
        self.datapoints = result['datapoints']
        if zero_missing:
            self.sorted = sorted([float(x[0]) if x[0] is not None else float(0) for x in self.datapoints])
        else:
            self.sorted = sorted([float(x[0]) for x in self.datapoints if x[0]])


    @property
    def avg(self):
        return sum(self.sorted) / len(self.sorted)

    @property
    def mean(self):
        return self.avg

    @property
    def median(self):
        return self.percentile(50)

    @property
    def min(self):
        '''Returns the lowest value in the series'''
        return self.sorted[0]

    @property
    def max(self):
        '''Returns the highest value in the series'''
        return self.sorted[len(self.sorted)-1]

    def percentile(self, n):
        '''Returns the Nth percentile'''
        x = int(round(len(self.sorted) * (n/100)))
        return self.sorted[x-1]



class GraphiteResultSet(object):
    '''Represent a collection of GraphiteResults'''
    results = {}

    def __init__(self, results, query):
        # Save query for future features (e.g. re-execute it to get png render, calculate integrals, etc)
        self.query = query
        for result in results:
            self.results[result['target']] = GraphiteResult(result, query.zero_missing)

    def __getitem__(self, k):
        return self.results[k]

    def __repr__(self):
        return unicode(self)

    def __unicode__(self):
        return u'<GraphiteResultSet ({0}): {1}>'.format(len(self.results.keys()), ', '.join(self.results.keys()))

    @property
    def avg(self):
        '''Returns dictionary with averaged series'''
        return dict([(k, v.avg) for k, v in self.results.iteritems()])

    @property
    def mean(self):
        return dict([(k, v.mean) for k, v in self.results.iteritems()])

    @property
    def median(self):
        return dict([(k, v.median) for k, v in self.results.iteritems()])


    @property
    def min(self):
        return dict([(k, v.min) for k, v in self.results.iteritems()])

    @property
    def max(self):
        return dict([(k, v.max) for k, v in self.results.iteritems()])

    def percentile(self, n):
        return dict([(k, v.percentile(n)) for k, v in self.results.iteritems()])
