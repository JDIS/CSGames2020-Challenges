from flask import Flask
from flask_bootstrap import Bootstrap
import sqlite3

app = Flask(__name__)
app.secret_key = 'NOTSECURE'

bootstrap = Bootstrap(app)
db = sqlite3.connect("file:north.db?mode=ro", uri=True, check_same_thread=False)
db.row_factory = sqlite3.Row # Fix the missing column header
db.text_factory = lambda b: b.decode(errors = 'ignore')

from app import routes