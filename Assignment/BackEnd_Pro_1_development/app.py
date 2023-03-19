from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        test_str = request.form['test_str']
        regex = request.form['regex']
        matches = re.findall(regex, test_str)
        return render_template('result.html', matches=matches)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
