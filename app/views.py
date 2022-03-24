from flask import render_template, request
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = request.args.get('name')
    msg = request.args.get('message')
    return render_template("index.html",
        title = 'TEST VASILIY KLIAZIMIN',
        user = user,
        msg = msg)