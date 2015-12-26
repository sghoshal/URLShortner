A simple project to learn Python for web development, Flask, Mongo, Heroku, virtualenv.

Flask is a framework used for web development on the server side.

Steps to run this app locally:

1. If you don't have virtualenv installed, you can do:
	$ sudo pip install virtualenv
2. Clone this repo.
3. cd to this project's home directory.
4. $ virtualenv venv
5. $ source venv/bin/activate
6. Use pip to install the packages - Flask
	$ (venv) pip install flask
7. $ (venv) python url_shortner.py
   Starts a server on localhost:5000
8. Go to localhost:5000 using your favorite browser. Enter the Handler and destination (redirect) URL including http/https.
   For eg: Handler - yo, URL - https://www.yahoo.com
9. localhost:5000/yo should redirect you to the Yahoo home page.

NOTES:
- The Handler, URL info is stored in MongoDB on a remote box(used MongoHQ for this)

To run the app on the internet, heroku web hosting was used. 
- Heroku login password was created
- gunicorn was installed, which is the web framework.
- A Procfile was decalared
- foreman start

- pip freeze > requirements.txt
- store your app in git
https://devcenter.heroku.com/articles/getting-started-with-python
