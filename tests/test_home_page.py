from boxberry_tests.pages.registration_page import RegistrationPage
import allure
from selene.support.shared import browser
from selene import have, by

@allure.title("Successful fill form")
def test_registration(setup_browser):
    registration_page = RegistrationPage()

    with allure.step('Open registrations form'):
        registration_page.open()

    with allure.step("Fill form"):
        registration_page.type_first_name('Mariya')
        registration_page.type_last_name('Zhurova')
        registration_page.type_email('mzhurova4@mail.ru')
        registration_page.type_gender()
        registration_page.type_fhone_nomber('9234324557')
        registration_page.type_date_of_birth('1990', '9', '04')
        registration_page.type_subjects('Maths')
        registration_page.type_hobbies()
        registration_page.type_picture('2012091208303549.png')
        registration_page.type_address('Tomsk, Altayskaya')
        registration_page.type_state('Haryana')
        registration_page.type_city('Panipat')
        registration_page.submit()

    with allure.step("Assert registred results"):
        registration_page.assert_registred_date(
        'Mariya Zhurova', 'mzhurova4@mail.ru', 'Female', '9234324557', '04 October,1990', 'Maths', 'Sports',
        '2012091208303549.png', 'Tomsk, Altayskaya', 'Haryana Panipat'
    )



