import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"


def getAllAsFile():
    response = requests.get(url)
    return response.json()
    
if __name__ == "__main__":
    with open("cso.json", "wt") as fp:
        print(json.dumps(getAllAsFile()), file=fp)
  


    

