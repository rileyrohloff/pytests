import requests as req
import json
import user_urls
from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv('domain')
username = os.getenv('username')
password = os.getenv('password')


def create_session(domainUrl):
    login = req.post(domainUrl)
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

    auth = {
    'sessionID':session
    }
    create_proj = req.post(f'https://rileyrohloff.my.workfront.com/attask/api/v10.0/project?updates={params}', headers=auth)
    response = create_proj.json()
    global proj_ID
    proj_ID = response['data']['ID']
    proj_name = response['data']['name']
    return proj_name

def create_task(name, session, proj):
    params = {
    'name':name,
    'projectID':proj,
    'status':'INP'
    }

    headers = {
    'sessionID':session
    }

    task_create = req.post(user_urls.create_task_url, params=params, headers=headers)
    response = task_create.json()
    global taskID
    taskID = response['data']['ID']
    task_name = response['data']['name']
    return task_name
def update_task(ID, session):

    params = {
    'status':'CPL'
    }
    headers = {
    'sessionID':session
    }

    update_task_put = req.put(user_urls.task_url + ID, headers=headers, params=params)
    response = update_task_put.json()
    return response['data']['status']

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

def closeTest(session,URL):
    session_auth = {
    'sessionID':session
    }
    logout_req = req.get(URL, headers=session_auth)
    response = logout_req.json()
    return response['data']


# def solution(N):
#     myList = []
#     if N % 2 != 0:
#         myList.append(0)
#     for i in range(int(N/2)):
#         myList.append(i + 1)
#         myList.append(-(i + 1))
#     return myList
#
#
# def solution_array(n):
#     indexCount = 0
#     n.sort()
#     # n.remove(0)
#     while n[indexCount] % 4 != 0:
#         indexCount += 1
#     return n[indexCount]
#
# test_list = [22, 15, 2, 1, 44, 16, 24]
#
# # solution()
# # print(solution_array(test_list))
#
# austin  = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# # austin.reverse()
#
# length = len(austin)
# counter = length - 1
# while counter >= 0:
#     newList = []
#     newList.append(austin[counter])
#     counter -= 1
#
# print(newList)
