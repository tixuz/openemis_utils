from config.config import usr, pwd, core_url, institution_codes, shifts
from selenium_example.fun_add_shift_to_institution import add_shift_to_institution
from selenium_example.fun_get_core_chrome import get_chrome
from selenium_example.fun_get_institution_encoded_link import get_institution_encoded_link
from selenium_example.fun_login_core import login_core

driver = get_chrome()
if driver is not None:
    is_core_present = login_core(usr, pwd, core_url, driver)

    if is_core_present == 1:
        for institution_code in institution_codes:
            institution_encoded_link = get_institution_encoded_link(core_url, institution_code, driver)
            if institution_encoded_link != "":
                for shift in shifts:
                    add_shift_to_institution(core_url, institution_encoded_link, shift, driver)
