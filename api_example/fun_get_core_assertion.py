import json
from datetime import datetime, timezone

import jwt
from dateutil.relativedelta import relativedelta

from config.config import iss, auth_url


def get_core_assertion(iss=iss, auth_url=auth_url):
    now = datetime.now(timezone.utc)
    now_utc = int((now - relativedelta(months=+6)).timestamp())
    later_utc = int((now + relativedelta(months=+6)).timestamp())

    load = {
        "iss":iss,
        "scope":"API",
        "aud":auth_url,
        "exp":later_utc,
        "iat":now_utc
    }
    payload_string = json.dumps(load, indent=4)
    payload = json.loads(payload_string)
    pemfile = open("../jwtRS256.key", 'r')
    keystring = pemfile.read()
    pemfile.close()
    assertion = jwt.encode(payload, keystring, algorithm='RS256')
    b = open("core_assertion.txt", "w")
    b.write(assertion)
    b.close()
    return assertion
