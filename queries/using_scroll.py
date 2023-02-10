from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

#search data
res = es.search(index="users",scroll="20m", size=500,
                body={"query":{"match_all":{}}})

#get scroll id
s_id = res["_scroll_id"]
size = res["hits"]["total"]["value"]

#start scrolling
while (size > 0):
    res = es.scroll(scroll_id=s_id, scroll = "20m")

    #cross-check
    s_id = res["_scroll_id"]
    size = len(res["hits"]["hits"])

    #print
    for doc in res["hits"]["hits"]:
        print(doc["_source"])
    print(len(res["hits"]["hits"]))
