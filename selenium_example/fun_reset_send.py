import time

from selenium.webdriver.common.by import By

from selenium_example.fun_button_click import button_click


def reset_send(driver):
    try:
        button_path = '//*[@id="reset"]'
        button_click(button_path, driver)
    except Exception as e:
        print("Reset Send Exception: {0} Message: {1}".format("my message", str(e)))
