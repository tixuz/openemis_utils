import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def add_shift_to_institution(core_url, institution_encoded_link, shift_name, driver):
    try:
        driver.get("{}/Institution/Institutions/{}/Shifts/add".format(core_url, institution_encoded_link))
        select = Select(driver.find_element(By.NAME, 'InstitutionShifts[shift_option_id]'))
        select.select_by_visible_text(shift_name)
        time.sleep(2)
        button = driver.find_element(By.NAME, 'submit')
        button.click()
        time.sleep(2)
    except NoSuchElementException as e:
        print("Selenium Exception: {0} Message: {1}".format("my message", str(e)))
