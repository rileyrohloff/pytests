import api_riley
import user_urls
from dotenv import load_dotenv

load_dotenv()

# given a environment, when loggin in we should get a 200 response code if successful
# def test_login():
#     assert api_riley.create_session(utilites.login_url) == 200
# # given proper access from a successful login, when a project is created, this should return the name of that project
# def test_proj():
#     assert api_riley.create_proj('PythonTests', api_riley.sessionID) == 'PythonTests'
# # given a new project, when a new task is created under that project, the result of the test should return the task's proj_name
# def test_task_create():
#     assert api_riley.create_task('Python Task', api_riley.sessionID, api_riley.proj_ID) == 'Python Task'
# # given a new task, when the task's status is change in Workfront, the result of this test should return the new Workfront status_code
# def test_task():
#     assert api_riley.update_task(api_riley.taskID, api_riley.sessionID) == 'CPL'
# # given a new project, when an update is made to the name of that project, this should return the new name as a result
# def test_update():
#     assert api_riley.update_proj(api_riley.proj_ID, api_riley.sessionID) == 'Update Test'
# # given the new updated project, when we delete that project, the result of the API call should be '200'
# def test_tearDown():
#     assert api_riley.tear_down(api_riley.proj_ID, api_riley.sessionID) == 200
# # given functional access, when logging out and closing the test, the result should be a fixed JSON value which is "{'success':True}"
# def test_closeSession():
#     assert api_riley.closeTest(api_riley.sessionID) == {'success':True}
