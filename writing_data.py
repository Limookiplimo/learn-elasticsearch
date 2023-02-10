from elasticsearch import Elasticsearch
from elasticsearch import helpers
from faker import Faker

fake=Faker()
es=Elasticsearch("http://localhost:9200")

actions = [
    {
        "_index":"users",
        "_source":{
            "name":fake.name(),
            "street":fake.street_address(),
            "city":fake.name(),
            "zip":fake.zipcode()
            }
        }
        for i in range(998)
    ]
res = helpers.bulk(es, actions)
print(res)
