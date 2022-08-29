import time

from selenium.webdriver.common.by import By


def button_click(button_path, driver):
    try:
        button = driver.find_element(By.XPATH, button_path)
        button.click()
        time.sleep(1)
    except Exception as e:
        print("Button Send Exception: {0} Message: {1}".format("my message", str(e)))
