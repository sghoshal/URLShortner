# From the python package flask, import the "Flask" constructor
from flask import Flask, redirect
from flask import request
#from pymongo import MongoClient
import pymongo

app = Flask(__name__)

#client = MongoClient()

mongodb_uri = 'mongodb://soum:1234@paulo.mongohq.com:10013/URLShortner'

   # pymongo.Connection creates a connection directly from the URI, performing
   # authentication using the provided user components if necessary.

try:
   client = pymongo.Connection(mongodb_uri)
except Exception, e:
   print e
   print('Error: Unable to connect to database.')
   client = None

db = client.URLShortner
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
	
	print collection.find_one({'handler': handler})
	print 'OUTSIDE IF'
	#if key in db.keys():
	if collection.find_one({'handler': handler}) is not None:
		print "ALREADY TAKEN", collection.find_one({'url': url})
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

