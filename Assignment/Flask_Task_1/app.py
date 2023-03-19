from flask import Flask
from flask import request, render_template


app=Flask(__name__)

@app.route("/Me")
def homeroute():
    return render_template("index.html")

@app.route("/",methods=["Get"])
def mainroute():
    usesrname=request.args.get('username')
    return "Returning Username in uppercase- "+str(usesrname).upper()

if __name__=='__main__':
    app.run()