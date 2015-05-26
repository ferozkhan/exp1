
import riak


class RiakBucket(object):
    def __init__(self, port=8087):
        self.port = port
        self.client = riak.RiakClient(port=self.port)


class Bucket(RiakBucket):
    def __init__(self):
        super(Bucket, self).__init__()

    def __call__(self):
        return self.client.bucket('app')
