from flask import Flask, url_for
from markupsafe import escape


app = Flask(__name__)
name = "Heljhum Enad"

@app.route("/")
def hello_flask():
    return "Hello Flask"

@app.route("/hello/<username>")
def show_username(username):
    return f"Welcome Mr {escape(username)}"

@app.route("/post/<int:post_id>")
def show_post_id(post_id):
    if post_id == 5000:
        # url_for is use for reversing url to navigate page to page
        return f"You need to go back in this link <a href={url_for('show_username', username=name)}>Back to Menu</a>"
