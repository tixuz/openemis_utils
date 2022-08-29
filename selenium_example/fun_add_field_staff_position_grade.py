from selenium.common import NoSuchElementException

from selenium_example.fun_go_to import go_to
from selenium_example.fun_select_send import select_send
from selenium_example.fun_submit_send import submit_send
from selenium_example.fun_text_send import text_send


def add_field_staff_position_grade(core_url, grade, driver):
    try:
        goto_url = "{}/FieldOptions/StaffPositionGrades/add"
        go_to(goto_url, core_url, driver)

        text_path = '//*[@id="staffpositiongrades-name"]'
        text_text = grade["name"]
        text_send(text_path, text_text, driver)

        try:
            if grade["default"]:
                select_path = '//*[@id="staffpositiongrades-default"]'
                select_text = "Yes"
                select_send(select_path, select_text, driver)
        except Exception as e:
            pass

        submit_send(driver)

    except NoSuchElementException as e:
        print("Selenium Exception: {0} Message: {1}".format("my message", str(e)))
    except Exception as e:
        print("Selenium Exception: {0} Message: {1}".format("my message", str(e)))
