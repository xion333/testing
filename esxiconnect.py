#!/usr/bin/python
import ssl
from pysphere import VIServer
default_context=ssl._create_default_https_context
server = VIServer()

try:
    ssl._create_default_https_context=ssl._create_unverified_context
    server.connect("s3cn3t.ddns.net", "", "")
    print "Connected to {}{}".format(server.get_server_type(),server.get_api_version())
finally:
    ssl._create_default_https_context = default_context
