from flask import Flask, render_template, request
import requests
import json
#this is an simple comment
app = Flask(__name__)

def get_meme():
    url = "https://meme-api.com/gimme"
    # Use `requests.get` instead of `requests.request`, and `.json()` to parse the response directly
    response = requests.get(url).json()
    meme_large = response["preview"][-2]  # Second last preview URL
    subreddit = response["subreddit"]
    return meme_large, subreddit

@app.route("/")
def index():
    meme_pic, subreddit = get_meme()
    return render_template("index.html", meme_pic=meme_pic, subreddit=subreddit)
