from config.config import usr, pwd, core_url, identity_types, nationalities, staff_position_grades, positions
from selenium_example.fun_add_field_identity_type import add_field_identity_type
from selenium_example.fun_add_field_nationality import add_field_nationality
from selenium_example.fun_add_field_staff_position import add_field_staff_position
from selenium_example.fun_add_field_staff_position_grade import add_field_staff_position_grade
from selenium_example.fun_get_core_chrome import get_chrome
from selenium_example.fun_login_core import login_core

driver = get_chrome()
if driver is not None:
    is_core_present = login_core(usr, pwd, core_url, driver)

    if is_core_present == 1:
        for identity_type in identity_types:
                    add_field_identity_type(core_url, identity_type, driver)
        for nationality in nationalities:
                    add_field_nationality(core_url, nationality, driver)
        for grade in staff_position_grades:
                    add_field_staff_position_grade(core_url, grade, driver)
        for position in positions:
                    add_field_staff_position(core_url, position, driver)
