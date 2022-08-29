path_to_chrome_driver = "../chromedriver"

# OpenEMIS Core
usr = "admin"
pwd = "demo"
core_url = "http://localhost:8082/core"
# core_url = "https://demo.openemis.org/core"
port = 9292

institution_codes = ["S2005",
                     "S1006",
                     "S2007"]

shifts = [
    {"name":"Morning Shift"},
    {"name":"All Day Long Shift"},
]

identity_types = [
    {"name":"National ID",
     "default":"Yes"},
    {"name":"Passport"}]

nationalities = [
    {"name":"Citizen",
     "identity":"National ID",
     "default":"Yes"},
    {"name":"Non-Citizen",
     "identity":"Passport"},
]

staff_position_grades = [
    {"name":"Pay Scale 1",
     "default":"Yes"}]

positions = [
    {"name":"Administrator",
     "security":"Administrator"},
    {"name":"Group Administrator",
     "security":"Group Administrator"},
    {"name":"Principal",
     "security":"Principal",
     "teaching":"Yes"},
    {"name":"Deputy Principal",
     "security":"Deputy Principal",
     "teaching":"Yes"},
    {"name":"Teacher",
     "security":"Teacher",
     "default":"Yes",
     "teaching":"Yes"},
    {"name":"Staff",
     "security":"Staff",
     "default":"Yes"},
]

area_levels = [
    {"name":"Zone"}
]


# API
iss = "1661484483-19e52a2fc99b634e.app"
auth_url = "https://demo.openemis.org/core/oauth/token"
api_url = "https://demo.openemis.org/core/restful/"
