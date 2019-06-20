import api_riley
import user_urls
from dotenv import load_dotenv
import unittest

class TestApi(unittest.TestCase):
    
    def test_firstUser(self):
        self.result = api_riley.create_session(user_urls.login_url)
        self.projectCheck = api_riley.create_proj('PythonTests', api_riley.sessionID)
        self.assertEqual(self.result, 200)
        self.assertEqual(self.projectCheck, 'PythonTests')