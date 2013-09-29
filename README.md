Script written in Python
Flask is a framework used for web development on the server side.
For this project, I set up the virtual environment on mac
$ virtualenv venv
$ source venv/bin/activate

Use pip to install the packages - Flask
$ (venv) pip install flask

The app can be run on local host, using Flask. 
Running
python url_shortner.py will start a server on localhost
Go to http://127.0.0.1:5000/ to see the home page of the app.

The app will let the user fill a form. When he clicks the submit 
button, it goes to form-response method defined by 
insert_into_db()

MongoDB has been used to store all the key value pairs. To use MongoDB from 
python, the PyMongo package was installed. Since MongoDB is a non relational 
database, the user's 'URL to be shortened' and the 'Shortened URL' is stored 
as a dictionary of keys and values.

To run the app on the internet, heroku web hosting was used. 
- Heroku login password was created
- gunicorn was installed, which is the web framework.
- A Procfile was decalared
- foreman start

- pip freeze > requirements.txt
- store your app in git
https://devcenter.heroku.com/articles/getting-started-with-python

- Since the app is hosted on the internet, MongoDB has to run on the 
  server. I used MongoHQ which MongoDB as a service. I created my account, 
  added an user and used the mongo_uri provided in the script

