from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "sosecret"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/preresult', methods=['POST'])
def button():
    session['name'] = request.form["name"]
    session['location'] = request.form["location"]
    session['language'] = request.form["language"]
    session['comment'] = request.form["comment"]
    if len(request.form['name']) > 0:
        flash("Success! Your name is {}".format(request.form['name']))
    else:
        flash("Name cannot be empty!")
        return redirect('/')
    if len(request.form['comment']) > 1:
        if len(request.form['comment']) < 120:
            flash("Success! Your comment is {}".format(request.form['comment']))
        else:
            flash("Too many characters in comment!")
            return redirect('/')
    else:
        print('fuck')
        flash("Comment cannot be empty")
        return redirect('/')
    return redirect('/result')

@app.route('/result')

def realresult():
    return render_template('/result.html')

app.run(debug=True)
