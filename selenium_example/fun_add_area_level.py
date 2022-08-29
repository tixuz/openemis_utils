from selenium.common import NoSuchElementException

from selenium_example.fun_go_to import go_to
from selenium_example.fun_select_send import select_send
from selenium_example.fun_submit_send import submit_send
from selenium_example.fun_text_send import text_send


def add_area_level(core_url, area_level, driver):
    try:
        goto_url = "{}/Areas/Levels/add"
        go_to(goto_url, core_url, driver)

        text_path = '//*[@id="arealevels-name"]'
        text_text = area_level["name"]
        text_send(text_path, text_text, driver)

        submit_send(driver)
    except NoSuchElementException as e:
        print("Nationality Exception: {0} Message: {1}".format("my message", str(e)))
    except Exception as e:
        print("Nationality Big Exception: {0} Message: {1}".format("my message", str(e)))
