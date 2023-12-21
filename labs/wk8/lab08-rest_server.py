from flask import Flask, url_for, request, redirect, abort, jsonify

app = Flask(__name__, static_url_path='', static_folder='staticpages')

books=[
    {"id": 1, "Title": "Harry Potter", "Author": "JK", "Price": 1000},
    {"id": 2, "Title": "some cook book", "Author": "Mr Angry Man", "Price": 2000},
    {"id": 3, "Title": "Python made easy", "Author": "Some Liar", "Price": 1500}
]

nextId=4

@app.route('/')
def index():
    return "hello"

#1.1 get all (curl GET)
@app.route('/books')
def getAll():
    return jsonify(books)

#1.2. find By id (curl GET)
@app.route('/books/<int:id>')
def findById(id):
    foundBooks = list(filter (lambda t : t["id"]== id, books))
    if len(foundBooks) == 0:
        return jsonify({}) , 204
    return jsonify(foundBooks[0])

#3. create (curl POST)
# curl -X POST -d "{\"Title\":\"test\", \"Author\":\"some guy\", \"Price\":123}" http://127.0.0.1:5000/books
@app.route('/books', methods=['POST'])
def create():
    global nextId
    # check the user posted a JSON object
    if not request.json:
        abort(400)
    # create an object with data in it. nextId to make sure the id doesn't exist 
    book = {
        "id": nextId,
        "Title": request.json["Title"],
        "Author": request.json["Author"],
        "Price": request.json["Price"]
    }
    books.append(book)
    nextId += 1
    return jsonify(book)

#4. update (curl PUT)
# curl -X PUT -d "{\"Title\":\"new Title\", \"Price\":999}" -H "content-type:application/json" http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    # searching for all books with given id. It may return more than 1 book, a list of books
    foundBooks = list(filter(lambda t: t["id"] == id, books))
    # check if list is not empty
    if len(foundBooks) == 0:
        return jsonify({}), 404
    # retreve only the first book in the list, currentBook is the book being updated 
    currentBook = foundBooks[0]
    # if attribute was uploaded, update that attribute
    if 'Title' in request.json:
        currentBook['Title'] = request.json['Title']
    if 'Author' in request.json:
        currentBook['Author'] = request.json['Author']
    if 'Price' in request.json:
        currentBook['Price'] = request.json['Price']

    # return the updated object
    return jsonify(currentBook)

#5. delete (curl DELETE)
# curl -X DELETE http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    # find the object to delete
    foundBooks = list(filter(lambda t: t["id"] == id, books))
    if len(foundBooks) == 0:
        return jsonify({}), 404
    # remove the object
    books.remove(foundBooks[0])

    return jsonify({"done":True})


if __name__ == "__main__":
    app.run(debug=True, port=8080)