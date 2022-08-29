import time


def go_to(goto_url, core_url, driver):
    try:
        driver.get(goto_url.format(core_url))
        time.sleep(1)
    except Exception as e:
        print("GoTO Exception: {0} Message: {1}".format("my message", str(e)))
