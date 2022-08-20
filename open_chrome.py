from selenium import webdriver
from selenium.common import TimeoutException, WebDriverException
from config import path_to_chrome_driver


def open_chrome(port, core_url):
    global driver
    opt = webdriver.ChromeOptions();
    argument = "--remote-debugging-port={}".format(str(port))
    opt.add_argument(argument)
    try:
        driver = webdriver.Chrome(path_to_chrome_driver,
                                  options=opt)
        driver.get(core_url)
        return driver
    except TimeoutException:
        print("Selenium Timeout 2")
        return None
    except WebDriverException as e:
        print("Selenium Exception 2: {0} Message: {1}".format("my message", str(e)))
        return None
