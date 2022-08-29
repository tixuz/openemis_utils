from selenium.common import NoSuchElementException

from selenium_example.fun_go_to import go_to
from selenium_example.fun_select_send import select_send
from selenium_example.fun_submit_send import submit_send
from selenium_example.fun_text_send import text_send


def add_field_nationality(core_url, nationality, driver):
    try:
        goto_url = "{}/FieldOptions/Nationalities/add"
        go_to(goto_url, core_url, driver)

        text_path = '//*[@id="nationalities-name"]'
        text_text = nationality["name"]
        text_send(text_path, text_text, driver)

        select_path = '//*[@id="nationalities-identity-identity_type-id"]'
        select_text = nationality["identity"]
        select_send(select_path, select_text, driver)

        try:
            if nationality["default"]:
                select_path = '//*[@id="nationalities-default"]'
                select_text = "Yes"
                select_send(select_path, select_text, driver)
        except Exception as e:
            pass
        submit_send(driver)
    except NoSuchElementException as e:
        print("Nationality Exception: {0} Message: {1}".format("my message", str(e)))
    except Exception as e:
        print("Nationality Big Exception: {0} Message: {1}".format("my message", str(e)))
