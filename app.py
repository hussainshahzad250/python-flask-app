from flask import Flask, request, abort
import socket

app = Flask(__name__)

@app.route("/")
def hello_world():
    hostname = socket.gethostname()
    html = f"<h1>This is python flask application !!</h1> This page is served from <b>{hostname}</b><hr>"
    return html

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=3000)
