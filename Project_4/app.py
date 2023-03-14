
from flask import Flask

app=Flask(__name__)

@app.route('/')

def home_page():
    return "Welcome to Homw Page"


@app.route('/search')

def search_page():
    return "welcome to the search page"


if __name__=='__main__':
    app.run()