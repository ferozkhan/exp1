import os

SERVICE_URL = 'http://datamall2.mytransport.sg/ltaodataservice/BusArrival'
SBS_SERVICES_URL = 'http://datamall.mytransport.sg/ltaodataservice.svc/SBSTInfoSet'
SMRT_SERVICES_URL = 'http://datamall.mytransport.sg/ltaodataservice.svc/SMRTInfoSet'

HEADERS = {
    'accept': 'application/json',
    'AccountKey': os.environ.get('AccountKey', ''),
    'UniqueUserID': os.environ.get('UniqueUserID', '')
}
