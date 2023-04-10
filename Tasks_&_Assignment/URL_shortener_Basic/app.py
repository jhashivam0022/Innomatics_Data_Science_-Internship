import os
from flask import Flask,render_template,request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pyshorteners


app=Flask(__name__)

shorter=""
url=""

basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
Migrate(app,db)


class DataBase(db.Model):
    __tablename__='urlshortener'
    id=db.Column(db.Integer,primary_key=True)
    url=db.Column(db.String(100))
    shorter = db.Column(db.String(100))
    
    def __init__(self,url,shorter):
        self.url=url
        self.shorter=shorter

        
@app.before_first_request
def create_tables():
    db.create_all()
    

@app.route('/',methods=["GET","POST"])
def index():
    global shorter,url
    if request.method=='POST':
        url=request.form.get('name')
        s_config=pyshorteners.Shortener()
        shorter=s_config.tinyurl.short(url)
        val=DataBase(url,shorter)
        db.session.add(val)
        db.session.commit()
        
    return render_template('index.html',s_url=shorter)

@app.route('/history')
def history():
    alllinks=DataBase.query.all()
    return render_template('history.html',alllinks=alllinks)


@app.route('/clear_history', methods=['POST'])
def clear_history():
    db.session.query(DataBase).delete()
    db.session.commit()
    return redirect(url_for('history'))

if __name__ == '__main__':
    app.run(debug=True)
