
import riak
import json
import requests
import itertools
from Constant import *
from multiprocessing import Pool


class Bucket(object):

    def __init__(self, port=8087):
        self.client = riak.RiakClient(port=port)

    def process_and_store(self, bucket, json_data):
        for data in json_data:
            key = '%s-%s' % (data['SI_SVC_NUM'], data['SI_SVC_DIR'])
            self.store(bucket, key, data)

    def store(self, bucket, key, data):
        container = bucket.new(key, data=data)
        container.store()


app_bucket = Bucket()


def bus_services_data():
    response_a = requests.get(SBS_SERVICES_URL, headers=HEADERS)
    response_b = requests.get(SMRT_SERVICES_URL, headers=HEADERS)
    total_bus_services = itertools.chain(
        json.loads(response_a.text)['d'],
        json.loads(response_b.text)['d'],
    )

    bus_service_bucket = app_bucket.client.bucket('bus_service_bucket')
    app_bucket.process_and_store(bus_service_bucket, total_bus_services)

if __name__ == "__main__":
    pool = Pool(5)
    r = pool.apply_async(bus_services_data)
    pool.close()
    pool.join()
    print r.get()
