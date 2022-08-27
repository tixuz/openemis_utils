from api_example.fun_get_core_assertion import get_core_assertion
from api_example.fun_get_core_bearer import get_core_bearer

assertion = get_core_assertion()
# print(assertion)
if assertion != "":
    bearer = get_core_bearer(assertion)
