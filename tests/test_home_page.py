from demoga_tests.pages.registration_page import RegistrationPage
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


def test_set_city(setup_browser):
        browser.open('')
        browser.element('.town__link').click()
        browser.all('[class="town-popup__item town-popup__item_active"]').element_by(have.text('Россия')).click()
        browser.element('[placeholder = "Поиск города"]').type('Томск')
        browser.element('[class="town-popup__item-city"]').click()

        browser.element('.town__link').should(have.text('Томск'))


def test_open_page_login_im(setup_browser):
        browser.open('')
        browser.element('[type = "button"]').click()
        browser.element('.header__profile').click()
        browser.all('[class="personal-accounts__text"]').element_by(have.text('Для интернет-магазинов')).click()
        browser.switch_to_previous_tab()

        browser.element('.login-reg__tab').should(have.text('Вход в личный кабинет'))


def test_login_im(setup_browser):
    browser.open('https://account.boxberry.ru/')
    browser.element('#authorizationform-email').type('ЛОГИН')
    browser.element('.login-reg').click()
 #   browser.element('.login-reg__tab selected').should(have.text('Вход в личный кабинет'))
    browser.element('.login-reg__tab').should(have.text('Регистрация'))