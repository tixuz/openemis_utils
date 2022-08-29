import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def select_send(select_path, select_text, driver):
    try:
        select_sender = Select(driver.find_element(By.XPATH, select_path))
        select_sender.select_by_visible_text(select_text)
        time.sleep(1)
    except Exception as e:
        print("Select Send Exception: {0} Message: {1}".format("my message", str(e)))
