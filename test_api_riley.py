import api_riley
import utilites
from dotenv import load_dotenv

load_dotenv()

def test_create_project():
    assert api_riley.create_project('pytest') == 200

def test_tear_down():
    assert api_riley.delete_item() == 200
