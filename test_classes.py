import api_riley
import utilites
from dotenv import load_dotenv
import unittest

class TestApi(unittest.TestCase):
    
    def test_login(self):
        result = api_riley.create_session()
        self.assertEqual(result, 200)