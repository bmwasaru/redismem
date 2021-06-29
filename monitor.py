from optparse import OptionParser
from time import sleep

import redis


def options():
    parser = OptionParser()
    parser.add_option("--host", default="localhost")
    parser.add_option("--port", type="int", default=6379)
    return parser.parse_args()


if __name__ == '__main__':
    (opts, args) = options()
    r = redis.Redis(host=opts.host, port=opts.port)
    um = 0

    while True:
        newum = r.info()['used_memory']
        if newum != um and um != 0:
            print(f"{um} bytes ({newum - um} difference)")
        um = newum
        sleep(1)
