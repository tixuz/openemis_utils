import time

from selenium.webdriver.common.by import By


def text_send(text_path, text_text, driver):
    try:
        text_sender = driver.find_element(By.XPATH, text_path)
        text_sender.send_keys(text_text)
        time.sleep(1)
    except Exception as e:
        print("Text Send Exception: {0} Message: {1}".format("my message", str(e)))
