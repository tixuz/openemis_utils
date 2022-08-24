import json
from datetime import datetime, timezone

import jwt
from dateutil.relativedelta import relativedelta

from config import iss, api_url

now = datetime.now(timezone.utc)
now_utc = int((now - relativedelta(months=+6)).timestamp())
later_utc = int((now + relativedelta(months=+6)).timestamp())

load = {
    "iss":iss,
    "scope":"API",
    "aud":api_url,
    "exp":later_utc,
    "iat":now_utc
}
payload_string = json.dumps(load, indent=4)
payload = json.loads(payload_string)
pemfile = open("jwtRS256.key", 'r')
keystring = pemfile.read()
pemfile.close()
token = jwt.encode(payload, keystring, algorithm='RS256')
b = open("core_assertion.txt", "w")
b.write(token)
b.close()
