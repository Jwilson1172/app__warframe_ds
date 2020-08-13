import unittest
from unittest import TestCase

from flask import Flask
from app import create_app


class test_server(TestCase):
    def __init__(self):
        self.server = create_app()
        return

    def test_init(self):
        try:
            self.assertIsInstance(self.server, type(Flask('None')))
            # check to see if the inital server url mapping is correct
            self.assertEqual(
                str(self.server.url_map),
                "Map([<Rule '/_dash-update-component' (POST, OPTIONS) -> /_dash-update-component>,\n <Rule '/_dash-dependencies' (HEAD, GET, OPTIONS) -> /_dash-dependencies>,\n <Rule '/_dash-layout' (HEAD, GET, OPTIONS) -> /_dash-layout>,\n <Rule '/_reload-hash' (HEAD, GET, OPTIONS) -> /_reload-hash>,\n <Rule '/_favicon.ico' (HEAD, GET, OPTIONS) -> /_favicon.ico>,\n <Rule '/' (HEAD, GET, OPTIONS) -> />,\n <Rule '/_dash-component-suites/<package_name>/<fingerprinted_path>' (HEAD, GET, OPTIONS) -> /_dash-component-suites/<string:package_name>/<path:fingerprinted_path>>,\n <Rule '/static/<filename>' (HEAD, GET, OPTIONS) -> static>,\n <Rule '/assets/<filename>' (HEAD, GET, OPTIONS) -> _dash_assets.static>,\n <Rule '/<path>' (HEAD, GET, OPTIONS) -> /<path:path>>])"
            )
        except AssertionError as ae:
            # passthrough falling tests to test handler
            raise ae
        except Exception as e:
            # else print error info and passthrough
            print("there was a problem with the logic of ", e)
            raise e
        return


if __name__ == "__main__":
    print("please use pytest to test application\n")
    print(
        "if you must REALLY test just one thing then go ahead and hit 'y' then enter"
    )
    if input("[y,n]: ").lower() == 'y':
        try:
            s = test_server()
            s.test_init()
        except AssertionError as ae:
            print(f"test failing at {ae}")
            raise ae
