from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def home_fun():
    return render_template('index.html')

@app.route('/about')
def about_fun():
    return render_template('about.html')

@app.route('/contact')
def contact_fun():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)