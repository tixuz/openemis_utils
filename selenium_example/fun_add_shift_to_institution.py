from selenium.common import NoSuchElementException

from selenium_example.fun_go_to import go_to
from selenium_example.fun_select_send import select_send
from selenium_example.fun_submit_send import submit_send


def add_shift_to_institution(core_url, institution_encoded_link, shift, driver):
    try:
        goto_url = "/Institution/Institutions/{}/Shifts/add".format(institution_encoded_link)
        goto_url = "{}" + goto_url
        go_to(goto_url, core_url, driver)

        select_path = '//*[@id="institutionshifts-shift-option-id"]'
        select_text = shift["name"]
        select_send(select_path, select_text, driver)

        submit_send(driver)
    except NoSuchElementException as e:
        print("Selenium Exception: {0} Message: {1}".format("my message", str(e)))
