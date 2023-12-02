import time

from boxberry_tests.pages.e_commerce_page import ECommercePage
import allure
from selene.support.shared import browser
from selene import have, by


def test_calculate_parcel_business_client(setup_browser):
    e_commerce_page = ECommercePage()
    e_commerce_page.open()
    browser.element('a.button.button_red').click()
    browser.element('.multiselect__placeholder').click()
    time.sleep(3)
    browser.element('input.multiselect__input').type('Екатеринбург').press_enter()
    browser.element('.multiselect__placeholder').click()
    time.sleep(3)
    browser.element('[placeholder="Город-получатель"]').type('Томск').press_enter()
    browser.element('[placeholder="Оценочная стоимость"]').type('0')
    browser.element('[placeholder="Высота"]').type('5')
    browser.element('[placeholder="Ширина"]').type('6')
    browser.element('[placeholder="Длина"]').type('7')
    browser.element('#calcWeight').type('11')

 #   browser.element('div[class="calculator-nav__inner"] a:nth-child(2)').click()

def test_show_point(setup_browser):
    e_commerce_page = ECommercePage()
    e_commerce_page.open()
    browser.element('#item-map-send > a.button.button_red').click()
    browser.element('.city-name').click()
    browser.element('.town-popup__list-wrap li:nth-child(4)').click()

    browser.element('.city-name').should(have.text('Новосибирск'))


def test_parcel_not_found(setup_browser):
    e_commerce_page = ECommercePage()
    e_commerce_page.open()
    browser.element('[placeholder="Трек-номер"]').type('5546456565645')
    browser.element('button.button').click()

    browser.element('.empty-search-result__title').should(have.text('Номер заказа не найден'))
