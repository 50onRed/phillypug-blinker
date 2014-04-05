from flask import Flask
from raven.contrib.flask import Sentry
from flask.signals import got_request_exception

app = Flask(__name__)

sentry = Sentry(dsn=app.config['SENTRY_DSN'])

@got_request_exception.connect
def log_exception_to_sentry(app, exception=None, **kwargs):
    """
    Logs an exception to sentry.

    :param app: The current application
    :param exception: The exception that occurred
    """
    sentry.captureException(exception)
