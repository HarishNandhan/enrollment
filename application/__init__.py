from flask import Flask 

app = Flask(__name__, static_url_path='/public', static_folder='static')

app.debug = True

from application import routes
