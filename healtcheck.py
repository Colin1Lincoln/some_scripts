#!/usr/bin/python3.6

import requests
import urllib3
import sys

from urllib3.exceptions import ConnectionError
from requests.exceptions import Timeout

try:
    http_request = "http://localhost:8001"

    response = requests.get(http_request, timeout=(3,3))

    if response.status_code == 200:
        print("healthy")
        sys.exit(0)
    elif response.status_code == 404:
        print("unhealthy: status code 404", file=sys.stderr )
        sys.exit(1)

    else:
        print("unhealthy", file=sys.stderr)
        sys.exit(1)

except Timeout:
    print("Connection is timeout", file=sys.stderr)
    sys.exit(1)

except requests.exceptions.ConnectionError:
    print("Couldn't connect to host -", http_request, file=sys.stderr)
    sys.exit(1)
