import os

import sentry_sdk
from dotenv import load_dotenv
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

load_dotenv()

SENTRY_DSN = os.getenv("SENTRY_DSN")
sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0
)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, This World!'


@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0
