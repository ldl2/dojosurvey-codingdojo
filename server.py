from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result')
def result():
    name = request.form["name"]
    location = request.form["location"]
    language = request.form["language"]
    comment = request.form["comment"]
    print(comment, language, location, name)
    return render_template("result.html", name=name)

@app.route('/button', methods=['POST'])
def button():
    return redirect('/result')

app.run(debug=True)
