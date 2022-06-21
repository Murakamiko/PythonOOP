from app import app
from flask import flask

class Cvcontroller():
    @app.route('/cv')
    def getcv():
        return render_template('cv/cv.html')