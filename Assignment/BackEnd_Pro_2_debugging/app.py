from flask import Flask, render_template, request,redirect,url_for

app = Flask(__name__)

notes = []
@app.route('/', methods=["POST","GET"])
def index():
    note = request.args.get("note")
    notes.append(note)
    return render_template("home.html", notes=notes)

@app.route("/clear", methods=["POST"])
def clear():
    notes.clear()
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)