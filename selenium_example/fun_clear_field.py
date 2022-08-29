from selenium.webdriver.common.by import By


def clear_field(field_path, driver):
    search_field = driver.find_element(By.XPATH, field_path)
    if search_field:
        search_field.clear()
