from pprint import pprint

import requests

from config import auth_url, api_url


def get_assertion():
    try:
        assertion_file = open("core_assertion.txt", 'r')
        assertion = assertion_file.read()
        assertion_file.close()
        return assertion
    except Exception as e:
        pprint(e)
        return ""


def get_bearer(assertion):
    try:
        # pprint(req.content)
        # pprint(req.json())
        auth_hed = {'Content-Type':'application/x-www-form-urlencoded'}
        auth_payloads = {'grant_type':'urn:ietf:params:oauth:grant-type:jwt-bearer', 'assertion':assertion}
        req = requests.post(auth_url, data=auth_payloads, headers=auth_hed)
        bearer = req.json()["access_token"]
        return bearer
    except Exception as e:
        pprint(e)
        return ""


def get_type_id(bearer, type_name):
    try:
        hed = {'Authorization':'Bearer ' + bearer}
        url = api_url + "Institution.Types"
        response = requests.get(url, headers=hed)
        types = response.json()['data']
        type_id = next(type['id'] for type in types if type['name'] == type_name)
        return type_id
    except Exception as e:
        pprint(e)
        return 0


def get_institution_codes(bearer, type_id):
    try:
        hed = {'Authorization':'Bearer ' + bearer}
        url = api_url + "Institution.Institutions?institution_type_id={}&_limit=0&_fields=code".format(str(type_id))
        response = requests.get(url, headers=hed)
        institutions = response.json()['data']
        mapcodes = map(lambda institution:institution['code'], institutions)
        codes = list(mapcodes)
        return codes
    except Exception as e:
        pprint(e)
        return []
