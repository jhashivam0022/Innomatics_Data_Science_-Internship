import os
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app=Flask(__name__)

basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
Migrate(app,db)

class subji(db.Model):
    __tablename__="names"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.Text)
    mrp=db.Column(db.Integer)

    def __init__(self,name,mrp):
        self.name=name
        self.mrp=mrp
    def __repr__(self):
        return "Name --{} and mrp -- {}".format(self.name,self.mrp)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/add')
def add():
    return render_template("add.html")

@app.route('/search')
def search():
    return render_template("search.html")

@app.route('/display')
def display():
    return render_template("display.html")


if __name__=="__main__":
    app.run(debug=True)