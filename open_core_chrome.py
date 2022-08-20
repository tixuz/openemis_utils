from selenium.webdriver.common.by import By

from add_institution_shifts import add_institution_shifts
from clear_field import clear_field
from selenium import webdriver
from selenium.common import TimeoutException, WebDriverException

from login_core import login_core
from open_chrome import open_chrome
from config import *
# # opt = webdriver.Chrome.create_options();
opt = webdriver.ChromeOptions();
# opt.add_argument("--remote-debugging-port=9292")
opt.add_experimental_option("debuggerAddress", "localhost:{}".format(str(port)))
driver = None

try:
    driver = webdriver.Chrome(executable_path=".//chromedriver",
                              options=opt)
except TimeoutException:
    print("Selenium Timeout")
    driver = open_chrome(port, core_url)
except WebDriverException as e:
    print("Selenium Exception: {0} Message: {1}".format("my message", str(e)))
    driver = open_chrome(port, core_url)

if driver != None:
    login_core(usr, pwd, core_url, driver)
    driver.get("{}/Institutions/Institutions/index".format(core_url))
    search_field_name = "Search[searchField]"
    clear_field(search_field_name,driver)
    search_class = "btn btn-default btn-xs btn-toggled"
    adv_search_button = driver.find_element(By.ID, "search-toggle")
    if adv_search_button.get_attribute("class") == search_class:
        print("found")
    else:
        adv_search_button.click()
    search_field_name = "AdvanceSearch[Institutions][tableField][code]"
    clear_field(search_field_name,driver)
    search_field_name = "AdvanceSearch[Institutions][tableField][name]"
    clear_field(search_field_name,driver)
    add_institution_shifts(core_url,institution_code,driver,first_shift,second_shift)
