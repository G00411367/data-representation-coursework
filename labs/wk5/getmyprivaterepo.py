import requests
import json
from config import config as cfg

filename = "repos-private-id.json"

url ='https://api.github.com/repos/G00411367/aprivateone'

apiKey = cfg["githubkey"]

response = requests.get(url, auth = ('token', apiKey))
print (response.status_code)

repoJSON = response.json()
#print (response.json())

with  open(filename, 'w') as fp:
    json.dump(repoJSON, fp, indent=4)
