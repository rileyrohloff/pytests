import requests as req
import json
import utilites
from dotenv import load_dotenv
import os

test_IDs = []

load_dotenv()

host = os.getenv('domain')
username = os.getenv('username')
password = os.getenv('password')

def create_session():

    login = req.post(utilites.login_url)
    response_login = login.json()
    return response_login['data']['sessionID']

def create_project(name):


    sessionID = create_session()


    params = {
    'name':name,
    'groupID':'5b15908a008d09a654a86358f25cc425',
    'status':'PLN'
    }

    createURL = f'{host}/attask/api/v10.0/project?updates={params}&sessionID={sessionID}'
    project_create_call = req.post(createURL)
    response = project_create_call.json()
    test_IDs.append(response['data']['ID'])

    statusCode = project_create_call.status_code


    if len(test_IDs) == 0:
        return False
    else:
        for ID in test_IDs:
            delete_proj_url_riley = f'https://rileyrohloff.my.workfront.com/attask/api/v10.0/project/{ID}&sessionID={sessionID}'
            delete_call = req.get(delete_proj_url_riley)
            response = delete_call.json()
            print(response)
            status_code = delete_call.status_code
            return status_code


create_project('testing')
