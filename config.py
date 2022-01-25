import os


class Config(object):
    # Twilio Client
    TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_ACCOUNT_TOKEN')

    # Twilio sync API credentials
    TWILIO_SYNC_SERVICE_SID = os.environ.get('TWILIO_SYNC_SERVICE_SID')
    TWILIO_SYNC_API_KEY = os.environ.get('TWILIO_SYNC_API_KEY')
    TWILIO_SYNC_API_SECRET = os.environ.get('TWILIO_SYNC_API_SECRET')

    # Heroku logs
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
