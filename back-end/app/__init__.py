from flask import Flask
from flask_cors import *

app = Flask(__name__)
CORS(app, supports_credentials=True)
from app import views