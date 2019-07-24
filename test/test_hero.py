import unittest
import requests

class TestHero(unittest.TestCase):

    def test_hero(self):
        request_json_body = requests.get('http://localhost:5000/Hero/Superman').json()
        assert request_json_body == 'Superman'

    def test_hero_fails(self):
        request_json_body = requests.get('http://localhost:5000/Hero/Robin').json()
        assert request_json_body == 'Batman'