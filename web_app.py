from flask import Flask, render_template
import requests
import json

app = Flask(__name__, static_url_path="/static")

def get_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.get(url).text)
    meme_large = response["preview"][-1]
    post_link = response["postLink"]
    return meme_large, post_link


@app.route("/")
def index():
    meme_pic, post_link = get_meme()
    return render_template("meme_index.html", meme_pic=meme_pic, post_link=post_link)

app.run(debug=True)