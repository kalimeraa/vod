import os
import tempfile
import pytest

from application import create_app,db

@pytest.fixture
def app():
    app = create_app(True)
    with app.app_context():
        import application.observer
        db.drop_all()
        db.create_all()
    
    yield app

@pytest.fixture
def client(app):
    """A test client for the app."""
    
    return app.test_client()