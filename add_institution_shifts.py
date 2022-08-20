import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def add_shift(core_url, data_row_id, driver, shift_name):
    try:
        driver.get("{}/Institution/Institutions/{}/Shifts/add".format(core_url, data_row_id))
        select = Select(driver.find_element('name', 'InstitutionShifts[shift_option_id]'))
        select.select_by_visible_text(shift_name)
        time.sleep(2)
        button = driver.find_element(By.NAME, 'submit')
        button.click()
        time.sleep(2)
    except NoSuchElementException as e:
        print("Selenium Exception: {0} Message: {1}".format("my message", str(e)))


def add_institution_shifts(core_url, institution_code, driver, first_shift, second_shift=""):
    # pass
    field_name = '//*[@id="advancesearch-institutions-code"]'
    search_field = driver.find_element(By.XPATH, field_name)
    if search_field:
        search_field.send_keys(institution_code)
    search_button = driver.find_element(By.XPATH, '//button[@data-original-title="Search"]')
    if search_field:
        search_button.click()

    table_class_name = "table table-curved table-sortable table-checkable"
    rows = driver.find_elements(By.XPATH, '//table[@class="{}"]/tbody/tr'.format(table_class_name))
    if len(rows) > 0:
        cells = rows[0].find_elements(By.XPATH, '//td');
        if len(cells) > 0:
            data_row_id = cells[0].get_attribute('data-row-id')
            print(data_row_id)
            add_shift(core_url, data_row_id, driver, first_shift)

            if second_shift != "":
                add_shift(core_url, data_row_id, driver, second_shift)
