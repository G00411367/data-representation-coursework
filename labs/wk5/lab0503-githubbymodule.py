import requests
from github import Github
from config import config as cfg

apikey = cfg["githubkeyc"]

g = Github(apikey)

#for repo in g.get_user().get_repos():
   #print(repo.name)

repo = g.get_repo("G00411367/testpygithub") 
#print(repo.clone_url) 

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print(urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.text
#print(contentOfFile)

newContents = contentOfFile + "more stuff \n"
print(newContents)

gitHubResponse = repo.update_file("test.txt", "updated by prog", newContents, fileInfo.sha)
print(gitHubResponse)