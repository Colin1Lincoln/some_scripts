#!/usr/bin/python3.6

import docker
from docker import client

docker_connect = client.Client(base_url='unix://var/run/docker.sock')
bwaf_container = docker_connect.inspect_container('bwaf-db')
status_bwaf_container = [log_value['Output'] for log_value in bwaf_container['State']['Health']['Log']]

status_code=(status_bwaf_container[(len(status_bwaf_container)-1)].strip())

if status_code == "healthy":
    print("5")
elif status_code == "unhealthy: status code 404":
    print("4")
elif status_code == "unhealthy":
    print("3")
elif status_code == "Connection is timeout":
    print("2")
elif status_code == "Couldn't connect to host - http://localhost:8001":
    print("1")
else:
    print(«0»)
