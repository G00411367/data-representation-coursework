import requests
# github module 
from github import Github
# config dictionary of keys
from config import config as cfg

# the key stored in a separate file; config.py
apikey = cfg["githubkey"]

# create github instance
g = Github(apikey)

# access the githunb repository
repo = g.get_repo("G00411367/data-representation-coursework") 
#print(repo.clone_url) 

# get the content of the file in repository
fileInfo = repo.get_contents("assignments/andrewFile.txt")

# file url
urlOfFile = fileInfo.download_url
#print(urlOfFile)

# store in response the HTTP get request from the file url (andrewFile.txt)
response = requests.get(urlOfFile)
# file content in text format
contentOfFile = response.text
#print(contentOfFile)

# modify the file content by replacing "Andrew" with "Ioan"
newContents = contentOfFile.replace("Andrew", "Ioan")
print(newContents)

# update the repo with modified file, comment 
gitHubResponse = repo.update_file("assignments/andrewFile.txt", "replace Andrew", newContents, fileInfo.sha)
print(gitHubResponse)