import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def add_field_nationality(core_url, nationality, driver):
    try:
        driver.get("{}/FieldOptions/Nationalities/add".format(core_url))
        name_path = '//*[@id="nationalities-name"]';
        name = driver.find_element(By.XPATH, name_path)
        name.send_keys(nationality["name"])
        time.sleep(1)
        identity_path = '//*[@id="nationalities-identity-type-id"]'
        select = Select(driver.find_element(By.XPATH, identity_path))
        select.select_by_visible_text(nationality["identity"])
        time.sleep(1)
        try:
            if nationality["default"]:
                default_path = '//*[@id="nationalities-default"]'
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
        print("Selenium Big Exception: {0} Message: {1}".format("my message", str(e)))
