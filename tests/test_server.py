from unittest import TestCase
from app import create_app


class TestServer(TestCase):

    app = create_app()

    def __init__(self):
        pass

    def test_init(self):
        r = self.app.get("/")
        self.assertEqual(r.status_code, 200)
