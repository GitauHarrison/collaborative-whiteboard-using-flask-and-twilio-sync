from app import app
from flask import render_template
from app.twilio_sync_api import _get_twilio_sync_access_token


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/whiteboard')
def whiteboard():
    return render_template('whiteboard.html')


@app.route('/token')
def token():
    return _get_twilio_sync_access_token()
