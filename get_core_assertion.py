from datetime import datetime,timezone
from pprint import pprint
import json
from dateutil.relativedelta import relativedelta
import jwt
now = datetime.now(timezone.utc)
now_utc = int((now - relativedelta(months=+6)).timestamp())
later_utc = int((now + relativedelta(months=+6)).timestamp())
iss = "1661320620-ce85d68ee926852c.app"
api_url = "https://demo.openemis.org/core/oauth/token"
load = {
  "iss": iss,
  "scope": "API",
  "aud": api_url,
  "exp": later_utc,
  "iat": now_utc
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
