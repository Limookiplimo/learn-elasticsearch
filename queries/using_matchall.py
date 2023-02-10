from elasticsearch import Elasticsearch

es=Elasticsearch("http://localhost:9200")
doc1 = {"query":{"match_all":{}}}
res = es.search(index="users", body=doc1, size=10)
print(res['hits']['hits'])