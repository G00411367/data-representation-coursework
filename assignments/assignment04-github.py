import requests
from github import Github
from config import config as cfg

apikey = cfg["githubkeyc"]

#apikey = ""

g = Github(apikey)

repo = g.get_repo("G00411367/data-representation-coursework") 
#print(repo.clone_url) 

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print(urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.text
#print(contentOfFile)