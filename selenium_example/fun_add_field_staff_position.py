from selenium.common import NoSuchElementException

from selenium_example.fun_go_to import go_to
from selenium_example.fun_select_send import select_send
from selenium_example.fun_submit_send import submit_send
from selenium_example.fun_text_send import text_send


def add_field_staff_position(core_url, position, driver):
    try:
        goto_url = "{}/FieldOptions/StaffPositionTitles/add"
        go_to(goto_url, core_url, driver)

        text_path = '//*[@id="staffpositiontitles-name"]'
        text_text = position["name"]
        text_send(text_path, text_text, driver)
        try:
            if position["teaching"]:
                select_path = '//*[@id="staffpositiontitles-type"]'
                select_text = "Teaching"
                select_send(select_path, select_text, driver)

        except Exception as e:
            select_path = '//*[@id="staffpositiontitles-type"]'
            select_text = "Non-Teaching"
            select_send(select_path, select_text, driver)

        try:
            if position["security"]:
                select_path = '//*[@id="staffpositiontitles-security-role-id"]'
                select_text = position["security"]
                select_send(select_path, select_text, driver)
        except Exception as e:
            pass

        try:
            select_path = '//*[@id="staffpositiontitles-position-grade-selection"]'
            select_text = 'Select All Position Grades'
            select_send(select_path, select_text, driver)
        except Exception as e:
            pass

        try:
            if position["default"]:
                select_path = '//*[@id="staffpositiontitles-default"]'
                select_text = "Yes"
                select_send(select_path, select_text, driver)
        except Exception as e:
            pass
        submit_send(driver)

    except NoSuchElementException as e:
        print("Staffpositiontitles Exception: {0} Message: {1}".format("my message", str(e)))
    except Exception as e:
        print("Staffpositiontitles Big Exception: {0} Message: {1}".format("my message", str(e)))
