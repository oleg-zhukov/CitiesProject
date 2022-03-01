from flask import Flask, request, render_template
from proj import call_process

app = Flask()


@app.route("/post", methods="POST")
def index():
    return call_process(request)


@app.route('/')
def main():
    return render_template('main.html')
