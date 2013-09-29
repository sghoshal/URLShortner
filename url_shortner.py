# From the python package flask, import the "Flask" constructor
from flask import Flask, redirect
from flask import request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient()
db = client.url_shortner
collection = db.urls

#db = {}
# Go to homepage() function here
@app.route("/")
def homepage():
    return """<form action="/form-response" method="post">
                Handler: <input type="text" name="handler">
                URL: <input type="text" name="url">
				<input type="submit" value="Submit">
              </form>"""

@app.route("/form-response", methods=['POST'])
def insert_into_db():
	handler = request.form['handler']
	url = request.form['url']
	
	#if key in db.keys():
	if collection.find_one({'handler': handler}) is not None:
		print collection.find_one({'url': url})
		return "The Handler is already been taken"
	else:
	    #db[key] = value
	    collection.insert({'handler': handler, 'url': url})
	return "The handler has been recorded"

@app.route("/<handler>") #, methods=['GET'])
def redirect_to_handler(handler=None):
	print 'HANDLER: ', handler
	print 'Value',  collection.find_one({'handler': handler})
	return redirect(str(collection.find_one({'handler': handler})[u'url']))

if __name__ == "__main__":
	app.run()

