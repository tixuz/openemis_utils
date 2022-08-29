import time

from selenium.webdriver.common.by import By


def submit_send(driver):
    try:
        button = driver.find_element(By.NAME, 'submit')
        button.click()
        time.sleep(1)
    except Exception as e:
        print("Submit Send Exception: {0} Message: {1}".format("my message", str(e)))
