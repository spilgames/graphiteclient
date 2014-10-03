graphiteclient
==============

# Example usage
q = GraphiteQuery('https://my-graphite-cluster.com', from='-24h')
q.add_target('my.stats.values', name='metric1')
q.add_target('my.stats.another', name='metric2')
results = q.run()

>>> print results
<GraphiteResultSet (2): metric1, metric2>

>>> print results.avg
{
  'metric1': 10,
  'metric2': 20,
}

>>> print results['metric1']
<GraphiteResult object at 0x1076fae50>

>>> print results['metric1'].avg
10

>>> print results['metric1'].datapoints
>>> print results['metric1'].sorted
[0, 10, 20]



# results.avg
# result
# result['metric1'].median()

>>> dir(results['metric1'])
['avg', 'percentile', 'median', 'etc']

