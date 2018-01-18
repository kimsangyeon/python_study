#parser.py

import requests
import psModule

#HTTP GET Request
req = requests.get('https://kimsangyeon.github.io/')

# get html source
html = req.text

# get http header
header = req.headers

# get http status
status = req.status_code
print 'HTTP Status Code : %d' % status

# get http status
reqOk = req.ok

# make Json
data = psModule.makeJson(html)

# make Json file
psModule.makeJsonFile(data)