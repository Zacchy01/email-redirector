from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def go():
    link = request.args.get('link', 'https://google.com')
    return redirect(link, code=302)