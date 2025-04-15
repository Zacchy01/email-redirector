from flask import Flask, request, redirect
import os

app = Flask(__name__)

@app.route('/')
def go():
    link = request.args.get('link', 'https://google.com')
    return redirect(link, code=302)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
