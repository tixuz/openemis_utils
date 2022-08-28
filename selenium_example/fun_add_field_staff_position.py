import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def add_field_staff_position(core_url, position, driver):
    try:
        driver.get("{}/FieldOptions/StaffPositionTitles/add".format(core_url))
        name = driver.find_element(By.XPATH, '//*[@id="staffpositiontitles-name"]')
        name.send_keys(position["name"])
        time.sleep(1)
        try:
            if position["teaching"]:
                pos_type_path = '//*[@id="staffpositiontitles-type"]'
                pos_type = Select(driver.find_element(By.XPATH, pos_type_path))
                pos_type.select_by_visible_text("Teaching")
                time.sleep(1)
        except Exception as e:
                pos_type_path = '//*[@id="staffpositiontitles-type"]'
                pos_type = Select(driver.find_element(By.XPATH, pos_type_path))
                pos_type.select_by_visible_text("Non-Teaching")
                time.sleep(1)
        try:
            if position["security"]:
                pos_sec_path = '//*[@id="staffpositiontitles-security-role-id"]'
                pos_sec = Select(driver.find_element(By.XPATH, pos_sec_path))
                pos_sec.select_by_visible_text(position["security"])
                time.sleep(1)
        except Exception as e:
            pass
        try:
            grade_path = '//*[@id="staffpositiontitles-position-grade-selection"]'
            grade = Select(driver.find_element(By.XPATH, grade_path))
            grade.select_by_visible_text('Select All Position Grades')
            time.sleep(1)
        except Exception as e:
            pass
        try:
            if position["default"]:
                default_path = '//*[@id="staffpositiontitles-default"]'
                default = Select(driver.find_element(By.XPATH, default_path))
                default.select_by_visible_text("Yes")
                time.sleep(1)
        except Exception as e:
            pass
        button = driver.find_element(By.NAME, 'submit')
        button.click()
        time.sleep(1)
    except NoSuchElementException as e:
        print("Selenium Exception: {0} Message: {1}".format("my message", str(e)))
    except Exception as e:
        print("Selenium Exception: {0} Message: {1}".format("my message", str(e)))
