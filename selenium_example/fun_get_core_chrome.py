from selenium import webdriver
from selenium.common import TimeoutException, WebDriverException

from config.config import port, core_url, path_to_chrome_driver
from open_chrome import open_chrome

opt = webdriver.ChromeOptions();
opt.add_experimental_option("debuggerAddress", "localhost:{}".format(str(port)))
driver = None


def get_chrome():
    try:
        driver = webdriver.Chrome(executable_path=path_to_chrome_driver,
                                  options=opt)
        return driver
    except TimeoutException:
        print("Selenium Timeout")
        driver = open_chrome(port, core_url)
        return driver
    except WebDriverException as e:
        print("Selenium Exception: {0} Message: {1}".format("my message", str(e)))
        driver = open_chrome(port, core_url)
        return driver
    return None
