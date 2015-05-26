
import requests
import json
import itertools


SERVICE_URL = 'http://datamall2.mytransport.sg/ltaodataservice/BusArrival'
SBS_SERVICES_URL = 'http://datamall.mytransport.sg/ltaodataservice.svc/SBSTInfoSet'
SMRT_SERVICES_URL = 'http://datamall.mytransport.sg/ltaodataservice.svc/SMRTInfoSet'

HEADERS = {
    'accept': 'application/json',
    'AccountKey': '',
    'UniqueUserID': ''
}


def list_bus_services():
    response_a = requests.get(SBS_SERVICES_URL, headers=HEADERS)
    response_b = requests.get(SMRT_SERVICES_URL, headers=HEADERS)
    total_bus_services = itertools.chain(
        json.loads(response_a.text)['d'],
        json.loads(response_b.text)['d'],
    )

    return [
        ((data['SI_SVC_NUM'], data['SI_SVC_DIR']), data)
        for data in total_bus_services
    ]


if __name__ == '__main__':
    import time
    start = time.time()
    import pprint
    pprint.pprint(list_bus_services())
    print('elapsed time : %10.7s' % (time.time() - start))
