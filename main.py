from flask import Flask, request, render_template
import os
from proj import call_process

app = Flask(__name__)


@app.route("/post", methods=["POST"])
def index():
    return call_process(request)


@app.route('/')
def main_page():
    return render_template('main.html')


def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
