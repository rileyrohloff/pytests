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
# Not sure why this is the case, however it looks like the pytest goes in alphabetical order. Hence why my last test is called zeleteObjects. If it is 'deleteObjects' the test runs first and fails.

    def test_zeleteObjects(self):
        self.deleteObjects = api_riley.tear_down(api_riley.proj_ID, api_riley.sessionID)
        self.assertEqual(self.deleteObjects, 200)

    def test_zz_closeTests(self):
        self.closeTesting = api_riley.closeTest(api_riley.sessionID, user_urls.logout_url)
        self.assertEqual(self.closeTesting, {'success': True})