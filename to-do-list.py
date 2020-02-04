from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config[ 'SQLALCHEMY_DATABASE_URI' ] = os.environ.get( 'DATABASE_URI' ) + '/todo'

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

class Task(db.Model):
  __tablename__ = 'tasks'
  id = db.Column( db.Integer, primary_key=True )
  description = db.Column( db.String( 64 ), unique=True )

db.create_all()

@app.route('/', methods=[ 'GET', 'POST' ])
def index():
  if request.method == 'POST':
    task = Task()
    task.description = request.form.get( 'description' )
    db.session.add( task )
    db.session.commit()
  tasks = db.session.query( Task ).all()
  return render_template( 'index.html', tasks=tasks )

@app.route('/remove/<string:description>', methods=[ 'GET', 'POST' ])
def remove(description):
  task = db.session.query( Task ).filter_by( description=description ).first()
  db.session.delete( task )
  db.session.commit()
  return redirect( url_for( 'index' ) )

app.run()
  