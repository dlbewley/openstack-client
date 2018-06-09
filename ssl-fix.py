#!/usr/bin/env python
"""
Fix up SSL validation API endpoints.
"""

import certifi
import requests
import os

#my_dir = os.path.dirname(os.path.realpath(__file__))
#custom_ca_bundle = 'certs/tls-ca-bundle.pem'
custom_ca_bundle = '/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem'

# however they are in this git repo also
sites = { 
    'https://openstack.example.com:13000/v3': custom_ca_bundle
}

for site,cert in sites.items():
    try:
        print('Checking connection to {}...'.format(site))
        test = requests.get(site)
        print('Connection OK.')
        print(test)
    except requests.exceptions.SSLError as err:
        cafile = certifi.where()
        print('Detected SSL Error. Adding custom certs to Certifi store {}'.format(cafile))

        with open(cert, 'rb') as infile:
            customca = infile.read()
        with open(cafile, 'ab') as outfile:
            outfile.write(customca)
        print('That might have worked. Run me again and find out.')
