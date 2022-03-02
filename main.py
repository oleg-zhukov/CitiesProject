from flask import Flask, request, render_template
from proj import call_process

app = Flask(__name__)


@app.route("/post", methods="POST")
def index():
    return call_process(request)


@app.route('/')
def main():
    return render_template('main.html')


if __name__ == "__main__":
    main()
