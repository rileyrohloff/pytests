import requests
from dotenv import load_dotenv
import os

load_dotenv()

domain = os.getenv('domain')
user = os.getenv('username')
password_user = os.getenv('password')

generate_api_key_url = 'http://%s/attask/api/v10.0/user?action=generateApiKey&username=%s&password=%s&method=PUT'
get_api_key_url = 'http://%s/attask/api/v10.0/user?action=getApiKey&username=%s&password=%s&method=PUT'
postbin_url = 'http://postbin.a-us-dev.wfk8s.com/postbins/'
event_sub_url = 'http://%s/attask/eventsubscription/api/v1/subscriptions'
create_proj_url = 'http://%s/attask/api/v10.0/%s'
delete_proj_url = f'http://domain/attask/api/v10.0/%s/%s'
delete_postbin_url = 'http://postbin.a-us-dev.wfk8s.com/postbins/%s'
login_url = f'https://rileyrohloff.my.workfront.com/attask/api/v10.0/login?username={user}&password={password_user}'
