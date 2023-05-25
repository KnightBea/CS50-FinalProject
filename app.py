from flask import Flask,render_template,redirect
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/quote')
def quote():
    response = requests.get("https://api.quotable.io/random")
    response = response.json()
    quotation = response["content"]
    author = response["author"]
    text = quotation + " - " + author
    return render_template("quote.html",text=text)

@app.route('/pomodoro')
def pomodoro():
    return render_template("timer.html")

@app.route('/scheduler', methods=['GET','POST','PUT'])
def scheduler():
    return render_template("scheduler.html")

if __name__ == "__main__":
    app.run(debug=True)