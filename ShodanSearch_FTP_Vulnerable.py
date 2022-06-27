#!/usr/bin/env python

import shodan
import re
import os

servers =[]
shodanKeyString = "euyiyVL4mbauNEjFj5NJD5vVMqdEiRET"
shodanApi = shodan.Shodan(shodanKeyString)

results = shodanApi.search("port: 21 Anonymous user logged in")
print("hosts number: " + str(len( results['matches'])))
for result in results['matches']:
	if result['ip_str'] is not None:
		servers.append(result['ip_str'])
		
for server in servers:
    print(server)