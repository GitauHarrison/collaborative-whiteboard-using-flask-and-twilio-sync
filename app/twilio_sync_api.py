from app import app
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import SyncGrant
from faker import Faker
from flask import jsonify, request


def _get_twilio_sync_access_token():
    # Create a fake username
    fake = Faker()
    username = request.args.get('username', fake.user_name())

    # Create access token with credentials
    token = AccessToken(
        app.config['TWILIO_ACCOUNT_SID'],
        app.config['TWILIO_SYNC_API_KEY'],
        app.config['TWILIO_SYNC_API_SECRET'],
        identity=username
    )
    # Create a Sync grant and add to token
    sync_grant = SyncGrant(app.config['TWILIO_SYNC_SERVICE_SID'])
    token.add_grant(sync_grant)
    return jsonify(identity=username, token=token.to_jwt())
