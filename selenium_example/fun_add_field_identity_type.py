import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def add_field_identity_type(core_url, type, driver):
    try:
        driver.get("{}/FieldOptions/IdentityTypes/add".format(core_url))
        name = driver.find_element(By.XPATH, '//*[@id="identitytypes-name"]')
        name.send_keys(type["name"])
        time.sleep(1)
        try:
            if type["default"]:
                default_path = '//*[@id="identitytypes-default"]'
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
