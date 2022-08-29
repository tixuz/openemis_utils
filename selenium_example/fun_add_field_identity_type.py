from selenium.common import NoSuchElementException

from selenium_example.fun_go_to import go_to
from selenium_example.fun_select_send import select_send
from selenium_example.fun_submit_send import submit_send
from selenium_example.fun_text_send import text_send


def add_field_identity_type(core_url, identity_type, driver):
    try:
        goto_url = "{}/FieldOptions/IdentityTypes/add"
        go_to(goto_url, core_url, driver)

        text_path = '//*[@id="identitytypes-name"]'
        text_text = identity_type["name"]
        text_send(text_path, text_text, driver)

        try:
            if identity_type["default"]:
                select_path = '//*[@id="identitytypes-default"]'
                select_text = "Yes"
                select_send(select_path, select_text, driver)
        except Exception as e:
            pass

        submit_send(driver)
    except NoSuchElementException as e:
        print("Identity Exception: {0} Message: {1}".format("my message", str(e)))
    except Exception as e:
        print("Identity Big Exception: {0} Message: {1}".format("my message", str(e)))
