import os
import signal
from flask import Flask
from fbbot import return_msg

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route("/")
def print_msg():
    page = '<html><body><h1>'
    page += return_msg('Hello World')
    page += '</h1></body></html>'
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT',5000)))

