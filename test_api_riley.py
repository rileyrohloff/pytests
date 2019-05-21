import api_riley

def test_api():
    assert api_riley.generate_key('https://rileyrohloff.my.workfront.com','APIuser@workfront.com','Password1') == True

def test_login_api():
    assert api_riley.login_api('https://rileyrohloff.my.workfront.com','APIuser@workfront.com','Password1') == True

def test_project_get():
    assert api_riley.get_project('https://rileyrohloff.my.workfront.com')