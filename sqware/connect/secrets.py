#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

Establishes Connection to Square API to allow access to store data for manipulation.
'''

import os
import json

	
#Global Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECURITY_KEY = os.path.join(BASE_DIR, 'secrets.json')

def get_secrets(setting):
	try:
		with open(SECURITY_KEY) as f:
			secrets = json.loads(f.read())
		return secrets[setting]
	except KeyError:
		return 'Variable not found. Please check json file and set the {0} environment variable.'.format(setting)






