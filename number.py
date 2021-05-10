from flask import Flask, render_template, redirect, session, request
import random

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"


@app.route('/')
def index():
    count = 0
    session['number'] = random.randint(1, 100)
    return render_template("index.html")

@app.route('/process_answer', methods = ['POST'])
def process_answer():
    message = ""
    form = request.form
    user_guess = form["guess"]
    if session['number'] == int(user_guess):
        message = "You win!"
    elif session['number'] > int(user_guess):
        message = "Too low"
    elif session['number'] < int(user_guess):
        message = "Too high"
    return render_template('index.html', message = message)

@app.route('/reset', methods = ['POST'])
def reset():
    session['number'] = random.randint(1, 100)
    return redirect('/')





if __name__ == "__main__":
    app.run(debug=True)