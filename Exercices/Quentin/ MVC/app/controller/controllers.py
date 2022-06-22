from app import app
from flask import render_template

class Controller:
    @app.route('/')
    def example():
        return render_template('example/example.html')