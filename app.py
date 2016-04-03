from flask import Flask, request, render_template
from flaskext.markdown import Markdown
from flask_sqlalchemy import SQLAlchemy
import os
from models import Destination
from database import db_session

app = Flask(__name__)
Markdown(app)

@app.route('/')
def index():
	names = Destination.query.all()
	destinations = []
	for name in names:
		destinations.append(name.to_dict())
	return render_template("home.html",names = destinations)

@app.route('/destination/<name>')
def render_destination(name):
	
	dest = Destination.query.filter(Destination.name == name).first()
	
	if not dest:
		return render_template("404.html", 404)	
	return render_template("destination.html", mkd=dest)



if __name__ == '__main__':
    if not os.path.isfile("cupidd.db"):
        import database
        database.init_db()
    
    app.run(debug=True)