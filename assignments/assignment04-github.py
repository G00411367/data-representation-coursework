import requests
from github import Github
from config import config as cfg

apikey = cfg["githubkey"]

#apikey = ""

g = Github(apikey)

repo = g.get_repo("G00411367/data-representation-coursework") 
#print(repo.clone_url) 

fileInfo = repo.get_contents("assignments/andrewFile.txt")
urlOfFile = fileInfo.download_url
#print(urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.text
#print(contentOfFile)

newContents = contentOfFile.replace("Andrew", "Ioan")
print(newContents)

gitHubResponse = repo.update_file("assignments/andrewFile.txt", "replace Andrew", newContents, fileInfo.sha)
print(gitHubResponse)