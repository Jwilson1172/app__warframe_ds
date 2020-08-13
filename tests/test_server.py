import unittest
from unittest import TestCase

from flask import Flask
from ..app import create_app


class test_server(TestCase):
    def __init__(self):
        self.server = create_app()
        return

    def test_init(self):
        try:
            self.assertIsInstance(server, Flask())
            self.assertTrue()
        except AssertionError as ae:
            raise ae
        except Exception as e:
            print("there was a problem with the logic of ", e)
