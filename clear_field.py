from selenium.webdriver.common.by import By


def clear_field(field_name, driver):
    search_field = driver.find_element(By.NAME, field_name)
    if search_field:
        search_field.clear()
