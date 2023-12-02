from boxberry_tests.pages.registration_page import RegistrationPage
import allure
from selene.support.shared import browser
from selene import have, by

def test_calculate_parcel_business_client(setup_browser):
    browser.open('e-commerce')
    browser.element('a.button.button_red').click()
   # browser.element('.multiselect__placeholder').click()
    browser.element('[class ="multiselect__tags"]').click()
    browser.element('input.multiselect__input').type('Екатеринбург').press_enter()
    #browser.element('[placeholder="Город-отправитель"]').type('Екатеринбург').press_enter()
    browser.element('[class ="multiselect__tags"]').click()
   # browser.element('.multiselect__placeholder').click()
    browser.element('[placeholder="Город-получатель"]').type('Томск').press_enter()
    browser.element('[placeholder="Оценочная стоимость"]').type('0')
    browser.element('[placeholder="Высота"]').type('5')
    browser.element('[placeholder="Ширина"]').type('6')
    browser.element('[placeholder="Длина"]').type('7')
    browser.element('#calcWeight').type('11')
 #   browser.element('div[class="calculator-nav__inner"] a:nth-child(2)').click()

#    browser.element('.end-information1__price').should(have.text('516 '))