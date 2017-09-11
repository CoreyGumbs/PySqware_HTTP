#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

Establishes Connection to Square API to allow access to store data for manipulation.
'''

import os
import json


#Globals
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
security_key = os.path.join(BASE_DIR, 'secrets.json')

print(BASE_DIR, security_key)


with open(security_key) as f:
	secrets = json.loads(f.read())
	print(secrets['ACCESS_TOKEN'])
