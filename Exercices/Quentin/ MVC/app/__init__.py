from flask import Flask
from flask_debugtoolbar import DebugToolbar
import psycopg2

app = Flask('app')
app.debug = True
app.secret_key = "Rg@O<z7Jd$C%j;C,aKD?O`8fwC(1$'E~"

toolbar = DebugToolbarExtension(app)

conn = psycopg2.connect(dbname='app', user='app', password='1234', host='127.0.0.1', port='5435')

from app.controllers import *