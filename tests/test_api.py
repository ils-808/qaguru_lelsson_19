import requests
import jsonschema

from utils.util import load_schema

BASE_URL = 'https://reqres.in/api/'

def test_users_list_success():
    schema = load_schema('list_users.json')
    resp = requests.get(f'{BASE_URL}users', params={'page':1})

    jsonschema.validate(resp.json(), schema)
    assert resp.status_code == 200

def test_user_not_found():
    resp = requests.get(f'{BASE_URL}users', params={23})

    assert resp.status_code == 404

def test_user_creation_success():
    schema = load_schema('user_creation.json')

    resp = requests.post(f'{BASE_URL}users', json={
            "name": "morpheus",
            "job": "leader"
    })

    jsonschema.validate(resp.json(), schema)
    assert resp.status_code == 201
    assert resp.json()['job'] == 'leader'

def test_user_change_title_success():
    schema = load_schema('user_update.json')

    resp = requests.put(f'{BASE_URL}users/2', json={
        "name": "morpheus",
        "job": "homeless"
    })

    jsonschema.validate(resp.json(), schema)
    assert resp.status_code == 200
    assert resp.json()['job'] == 'homeless'

def test_register_unsuccesfull():
    schema = load_schema('unsuccesfull_registration.json')

    resp = requests.post(f'{BASE_URL}register', json={
    "email": "sydney@fife"
})

    jsonschema.validate(resp.json(), schema)
    assert resp.status_code == 400
