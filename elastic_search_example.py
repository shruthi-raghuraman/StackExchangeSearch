#
# 1. Load the data from the XML using xml tree to a python object
#    Mostlikely it will be a list of objects.
#
# 2. For each member of the list of object (data) from the XML,
#    we want to index it in the elastic elasticsearch
#
# 3. Firs of all lets use the default indexing strategy
# 4. See the performance of behavior and then we can learn more about
#    configuring cusotm indexing or some advance feature


from elasticsearch import Elasticsearch

try:
  es = Elasticsearch()
  print ("Connected", es.info())
except Exception as ex:
  print ("Error:", ex)

es.index(index='test_index', doc_type='post', id=1, body={
  'author': 'John Doe',
  'blog': 'Learning Elasticsearch',
  'title': 'Using Python with Elasticsearch',
  'tags': ['python', 'elasticsearch', 'tips'],
  })

result = es.search(index='test_index', body={
    "query": {
        "bool": {
            "must": [{
                "match": { "author": "python" }
            }, {
                "match": { "title": "python" }
            }]
        }
    }
})
import pdb; pdb.set_trace()
