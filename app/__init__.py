# -*- coding: utf-8 -*-
"""Main application package."""

from flask import Flask
from app.dashboard import register_dashboard


def create_app():
    """Application factory for the Flask backend serving the dashboard.
    Avoid making changes here unless you are familiar with flask applications.
    """
    app = Flask(__name__)

    register_dashboard(app)

    return app
