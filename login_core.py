from selenium.common import WebDriverException, TimeoutException

def login_core(usr, pwd, core_url, driver):
    try:
        driver.get(core_url)
        username = driver.find_element('name', "username")
        username.clear()
        username.send_keys(usr)
        password = driver.find_element('name', "password")
        password.clear()
        password.send_keys(pwd)
        driver.find_element('name', 'submit').click()
        return 1
    except TimeoutException:
        print("Selenium Timeout 3")
        return 0
    except WebDriverException as e:
        print("Selenium Exception 3: {0} Message: {1}".format("my message", str(e)))
        return 0
