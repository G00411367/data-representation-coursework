import requests
import json

#1
url = "http://google.com"
response = requests.get(url)
#print(response.text)

#2
URL = "http://andrewbeatty1.pythonanywhere.com/books"
response = requests.get(URL)
#print(response.json())

#3
def readbooks():
    response = requests.get(URL)
    return response.json()

#4 
def readbook(id):
    geturl = URL + "/" +str(id)
    response = requests.get(geturl)
    # check the correct response
    print(response.status_code)
    return response.json()

#5
def createbook(book):
    response = requests.post(URL, json=book)
    # check the correct status code
    if response.status_code == 200:
        return response.json()
    else:
        print("Error in creating a book")

#6
def updatebook(id, bookdiff):
    puturl = URL + "/" + str(id)
    response = requests.put(puturl, json=bookdiff)
    return response.json()

#7
def deletebook(id):
    deleteurl = URL + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()

def getAllBooks():
    response = requests.get(URL)
    return response.json()

if __name__ == "__main__":
    book = {
        'Autor': "Status Code",
        'Title' : "Test Status",
        "Price" : 250
        }
    bookdiff = {
        "Price" : 12000
        }
    #print(readbooks())
    #print(readbook(355))
    #print(createbook(book))
    print(updatebook(360, bookdiff))
    print(deletebook(360))


