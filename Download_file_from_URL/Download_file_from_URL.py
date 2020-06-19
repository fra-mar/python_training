# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 21:45:22 2020

@author: marti
"""
#How to download a file from a URL. I copied this exemple from stackoverflow

import requests, os
import http.client

http.client.HTTPConnection._http_vsn = 10
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'

url="https://www.arcgis.com/sharing/rest/content/items/b5e7488e117749c19881cce45db13f7e/data"

print("Downloading...")
resp = requests.get(url)
with open('test.xls', 'wb') as output:
    output.write(resp.content)
print("Done!")
print ()