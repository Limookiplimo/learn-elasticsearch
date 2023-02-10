from elasticsearch import Elasticsearch
from pandas import json_normalize

es=Elasticsearch("http://localhost:9200")

doc2 = {"query":{"match":{"city":"Richard"}}}
res = es.search(index="users", body=doc2, size=10)

df = json_normalize(res['hits']['hits'])
print(df)