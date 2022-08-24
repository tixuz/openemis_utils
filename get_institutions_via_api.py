from pprint import pprint

from core_api_utils import get_assertion, get_bearer, get_type_id, get_institution_codes

bearer = ""
type_id = 0

assertion = get_assertion()
# print(assertion)
if assertion != "":
    bearer = get_bearer(assertion)
if bearer != "":
    type_name = 'Upper Secondary'
    type_id = get_type_id(bearer=bearer, type_name=type_name)
if type_id != 0:
    codes = get_institution_codes(bearer=bearer, type_id=type_id)
    pprint(codes)
