# You can create your own api requests to get data using example functions below

from pprint import pprint

import requests

from config.config import api_url


def get_institution_type_id(bearer, type_name):
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
