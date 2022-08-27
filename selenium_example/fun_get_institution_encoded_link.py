from selenium.webdriver.common.by import By

from selenium_example.fun_clear_field import clear_field


def get_institution_encoded_link(core_url, institution_code, driver):
    driver.get("{}/Institutions/Institutions/index".format(core_url))
    search_field_name = "Search[searchField]"
    clear_field(search_field_name, driver)
    search_class = "btn btn-default btn-xs btn-toggled"
    adv_search_button = driver.find_element(By.ID, "search-toggle")
    if adv_search_button.get_attribute("class") == search_class:
        print("found")
    else:
        adv_search_button.click()
    search_field_name = "AdvanceSearch[Institutions][tableField][code]"
    clear_field(search_field_name, driver)
    search_field_name = "AdvanceSearch[Institutions][tableField][name]"
    clear_field(search_field_name, driver)
    field_name = '//*[@id="advancesearch-institutions-code"]'
    search_field = driver.find_element(By.XPATH, field_name)
    institution_encoded_link = ""
    if search_field:
        search_field.send_keys(institution_code)
        search_button = driver.find_element(By.XPATH, '//button[@data-original-title="Search"]')
        if search_field:
            search_button.click()
        else:
            return institution_encoded_link
    else:
        return institution_encoded_link

    table_class_name = "table table-curved table-sortable table-checkable"
    rows = driver.find_elements(By.XPATH, '//table[@class="{}"]/tbody/tr'.format(table_class_name))
    if len(rows) > 0:
        cells = rows[0].find_elements(By.XPATH, '//td');
        if len(cells) > 0:
            institution_encoded_link = cells[0].get_attribute('data-row-id')
            return institution_encoded_link
        else:
            return institution_encoded_link
    else:
        return institution_encoded_link
