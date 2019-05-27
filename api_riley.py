import requests as req
import json
import utilites
from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv('domain')
username = os.getenv('username')
password = os.getenv('password')


def create_session():
    login = req.post(utilites.login_url)
    response = login.json()
    global sessionID
    sessionID = response['data']['sessionID']
    return login.status_code

def create_proj(name, session):

    params = {
    'name':name,
    'status':'PLN',
    'groupID':'5b9534860397593c6ee5fdbe2b578ede'
    }

    create_proj = req.post(f'https://rileyrohloff.my.workfront.com/attask/api/v10.0/project?updates={params}&sessionID={session}')
    response = create_proj.json()
    global proj_ID
    proj_ID = response['data']['ID']
    proj_name = response['data']['name']
    return proj_name

def update_proj(ID, session):

    update = {
    'name':'Update Test'
    }

    update_post = req.put(f"https://rileyrohloff.my.workfront.com/attask/api/v10.0/project/{ID}?updates={update}&sessionID={session}")
    response = update_post.json()
    proj_name = response['data']['name']
    return proj_name

def tear_down(ID, session_3):
    delete_proj = req.delete(f"https://rileyrohloff.my.workfront.com/attask/api/v10.0/project/{ID}?sessionID={session_3}")
    response = delete_proj.json()
    print(response)
    return delete_proj.status_code
