import api_riley
import utilites
from dotenv import load_dotenv

load_dotenv()


def test_login():
    assert api_riley.create_session() == 200

def test_proj():
    assert api_riley.create_proj('PythonTests', api_riley.sessionID) == 'PythonTests'

def test_update():
    assert api_riley.update_proj(api_riley.proj_ID, api_riley.sessionID) == 'Update Test'
def test_tearDown():
    assert api_riley.tear_down(api_riley.proj_ID, api_riley.sessionID) == 200
