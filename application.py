from flask import Flask, render_template, request
from AB import check_input, check_answer, generate_answer
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/check/", methods=['GET', 'POST'])
def check():
    if request.methods == 'POST':
        guess = request.form.get("guess")