import html

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return f"Hello {html.escape(request.args.get('name'))}! {html.escape(request.args.get('message'))}!"


if __name__ == "__main__":
    app.run()
