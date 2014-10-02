graphiteclient
==============

Flow / pseudo code:

```python
class GraphiteQuery(object):

    qattr = {}

    def __setattr__(self, attr, value): 
        self.qattr[attr] = value

# Example usage
q = GraphiteQuery('https://my-graphite-cluster.com')
q.add_target('my.stats.values', name='metric1')
q.add_target('my.stats.another', name='metric2')
q.from = '-24h'
q.end = 'now'
results = q.run()

>>> print results:
{
    'metric1': <GraphiteResult>,
    'metric2': <GraphiteResult>,
}
 
# result['metric1'].avg()
# result['metric1'].upper_90()
# result['metric1'].median()

>>> dir(results['metric1'])
['avg', 'upper_90', 'median', 'etc']

q = GraphiteQuery('https://my-graphite-cluster.com')
result = q.run_target('my.stats.values', from='-24h', end='now')
# print result
<GraphiteResult@a4x0dc1>

```
