from selenium.webdriver.common.by import By

from selenium_example.fun_button_click import button_click
from selenium_example.fun_go_to import go_to
from selenium_example.fun_reset_send import reset_send
from selenium_example.fun_text_send import text_send


def get_institution_encoded_link(institution_code, core_url, driver):
    institution_encoded_link = ""
    goto_url = "{}/Institutions/Institutions/index"
    go_to(goto_url, core_url, driver)

    button_path = '//*[@id="search-toggle"]'
    button_click(button_path, driver)
    reset_send(driver)

    button_path = '//*[@id="search-toggle"]'
    button_click(button_path, driver)

    text_path = '//*[@id="advancesearch-institutions-code"]'
    text_text = institution_code
    print(institution_code)
    text_send(text_path, text_text, driver)
    button_path = '//button[@data-original-title="Search"]'
    button_click(button_path, driver)
    table_class_name = "table table-curved table-sortable table-checkable"
    rows = driver.find_elements(By.XPATH, '//table[@class="{}"]/tbody/tr'.format(table_class_name))

    if len(rows) > 0:
        cells = rows[0].find_elements(By.XPATH, '//td');
        if len(cells) > 0:
            institution_encoded_link = cells[0].get_attribute('data-row-id')
            print(institution_encoded_link)
            return institution_encoded_link
        else:
            print("No Cells")
            return institution_encoded_link
    else:
        print("No Rows")
        return institution_encoded_link
