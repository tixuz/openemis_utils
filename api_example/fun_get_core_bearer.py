from pprint import pprint

import requests

from config.config import auth_url


def get_core_bearer(assertion):
    try:
        auth_hed = {'Content-Type':'application/x-www-form-urlencoded'}
        auth_payloads = {'grant_type':'urn:ietf:params:oauth:grant-type:jwt-bearer', 'assertion':assertion}
        req = requests.post(auth_url, data=auth_payloads, headers=auth_hed)
        bearer = req.json()["access_token"]
        b = open("core_bearer.txt", "w")
        b.write(bearer)
        b.close()
        return bearer
    except Exception as e:
        pprint(e)
        return ""
