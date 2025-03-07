# testcase 1: Add v1 on one node, do lookup on v1 on other nodes
# expected true

import requests
import time

newVertex = {"vertexName": "v1"}

url = "http://localhost:"
node1_port = "8080"
node2_port = "8081"
node3_port = "8082"
addvertex_endpoint = "/addvertex"
lookupvertex_endpoint = "/lookupvertex"

print("adding vertex " + newVertex['vertexName'] + " on node with port " + node1_port)
r1 = requests.post(url + node1_port + addvertex_endpoint, json=newVertex)

print(r1.text)

if (r1.text == "true"):
    print("succesfully added vertex " + newVertex['vertexName'] + " to node on port " + node1_port)
    print("waiting 2 seconds for synchronization")
    time.sleep(2)

    print("looking up vertex " + newVertex['vertexName'] + " on all nodes")
    r1 = requests.get(url + node1_port + lookupvertex_endpoint + "?vertexName=" + newVertex['vertexName'])
    r2 = requests.get(url + node2_port + lookupvertex_endpoint + "?vertexName=" + newVertex['vertexName'])
    r3 = requests.get(url + node3_port + lookupvertex_endpoint + "?vertexName=" + newVertex['vertexName'])

    print(r1.text)
    print(r2.text)
    print(r3.text)

    if (r2.text == "true" and r3.text == "true"):
        print("Node " + newVertex['vertexName'] + " now exists on all nodes")
