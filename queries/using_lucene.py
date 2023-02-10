from elasticsearch import Elasticsearch


es=Elasticsearch("http://localhost:9200")

res = es.search(index="users", q="name:caitlin Huber", size=10)
print(res['hits']['hits'])