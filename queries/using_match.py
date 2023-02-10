from elasticsearch import Elasticsearch
es=Elasticsearch("http://localhost:9200")



doc2 = {"query":{"match":{"city":"Richard"}}}

res = es.search(index="users", body=doc2, size=10)


for doc in res['hits']['hits']:
    print(doc['_source'])

# print(res['hits']['hits'])

