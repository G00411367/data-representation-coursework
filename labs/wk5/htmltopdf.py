import requests
import urllib.parse
from config import config as cfg

targetUrl = "https://en.wikipedia.org"
#apiKey = "4SLtqcqZni8hgu0bQtCLtGYvRegRSKV4XibObVAu7qtTypsHwYTz3gIvGObQGneq"
apiurl = 'https://api.html2pdf.app/v1/generate'

apiKey = cfg["htmltopdfkey"]


#requestUrl = apiurl + "?html=" + targetUrl + "&apiKey=" + apiKey

params = {'url': targetUrl,'apiKey': apiKey} 
parsedparams = urllib.parse.urlencode(params) 
requestUrl = apiurl +"?" + parsedparams 

response = requests.get(requestUrl)
print(response.status_code)

result = response.content
with open("document.pdf", "wb") as handler:
    handler.write(result)
