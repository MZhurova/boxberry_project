from boxberry_tests.pages.main_page import MainPage
import allure
from selene.support.shared import browser
from selene import have, by


def test_set_city(setup_browser):
        main_page = MainPage()
        main_page.open()
        browser.element('.town__link').click()
        browser.all('[class="town-popup__item town-popup__item_active"]').element_by(have.text('Россия')).click()
        browser.element('[placeholder = "Поиск города"]').type('Томск')
        browser.element('[class="town-popup__item-city"]').click()

        browser.element('.town__link').should(have.text('Томск'))


def test_open_page_login_im(setup_browser):
        main_page = MainPage()
        main_page.open()
        browser.element('[type = "button"]').click()
        browser.element('.header__profile').click()
        browser.all('[class="personal-accounts__text"]').element_by(have.text('Для интернет-магазинов')).click()
        browser.switch_to_previous_tab()

        browser.element('.login-reg__tab').should(have.text('Вход в личный кабинет'))


def test_parcel_search(setup_browser):
        main_page = MainPage()
        main_page.open()
        browser.element('.field-input__inner.form-bar-desktop__input').type('ACND280139442')
        browser.element('[aria-label="Поиск"]').click()

        browser.element('.track-details-item__body').should(have.text('Получена информация о заказе. Отправление еще не передано на доставку в Boxberry'))


def test_login_im(setup_browser):
    browser.open('https://account.boxberry.ru/')
    browser.element('#authorizationform-email').type('ЛОГИН')
    browser.element('.recaptcha-checkbox-border').click()
    browser.element('.btn-auth js-login-btn').click()

 #   browser.element('.login-reg__tab selected').should(have.text('Вход в личный кабинет'))
 #   browser.element('.login-reg__tab').should(have.text('Регистрация'))
