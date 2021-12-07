from flask import Flask, render_template, request, redirect, url_for
import requests
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    current_date=datetime.datetime.now().strftime("%Y-%m-%d")
    rover = request.args.get("rover","curiosity")
    date = request.args.get("Date","2015-12-03")
    response = requests.get(f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos?earth_date={date}&api_key=DEMO_KEY")
    data = response.json()
    
    return render_template('index.html', landing_image=data["photos"][0]["img_src"], current_date=current_date)

