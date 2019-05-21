import requests as req
import json

def generate_key(domain,username,password):
    generate_apiKey = req.get(f"{domain}/attask/api/v10.0/user?action=generateApiKey&method=PUT&username={username}&password={password}")
    response = generate_apiKey.json()
    if 'error' in response:
        return False
    else:
        return True

def login_api(domain,userName, Password):
    login = req.post(f"{domain}/attask/api/v10.0/login?username={userName}&password={Password}")
    response = login.json()
    if len(response['data']['sessionID']) != 0:
        return True
        return response['data']['sessionID']
    else:
        return False
    
def get_project(domain):
    sessionID = login_api('https://rileyrohloff.my.workfront.com','username','username')
    get_projects = req.get(f"{domain}/attask/api-unsupported/project/search?fields=ID&sessionID={sessionID}")
    response = get_projects.json()
    if 'data' in response:
        return True
    else:
        return False