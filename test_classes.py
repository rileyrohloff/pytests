import api_riley
import user_urls
from dotenv import load_dotenv
import unittest

class TestApi(unittest.TestCase):
    
    def test_firstUser(self):
        self.result = api_riley.create_session(user_urls.login_url)
        self.assertEqual(self.result, 200)

    def test_project(self):
        self.projectCheck = api_riley.create_proj('PythonTests', api_riley.sessionID)
        self.assertEqual(self.projectCheck, 'PythonTests')

    def test_task(self):
        self.create_Task = api_riley.create_task('API health', api_riley.sessionID, api_riley.proj_ID)
        self.assertEqual(self.create_Task, 'API health')
    def test_updateTask(self):
        self.updateTask = api_riley.update_task(api_riley.taskID, api_riley.sessionID)
        self.assertEqual(self.updateTask, 'CPL')