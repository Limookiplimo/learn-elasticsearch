from elasticsearch import Elasticsearch


es=Elasticsearch("http://localhost:9200")

doc = {"query":{"bool":{"must":{"match":{"city":"Richard"}},"filter":{"term":{"zip":"65822"}}}}}
res = es.search(index="users", body=doc, size=10)
print(res['hits']['hits'])