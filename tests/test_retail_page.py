import allure
from selene.support.shared import browser
from selene import have

def test_calculate_parcel_retail_client(setup_browser):
    browser.open('castnym-klientam/dostavka/otpravit_posylku')
    browser.element('.cta__button').click()
    browser.element('[name="sender"]').type('Екатеринбург (Свердловская)')
    browser.element('[name="receiver"]').type('Томск (Томская)')
    browser.element('[name="publicPrice"]').type('0')
    browser.element('[data-handler="renderPackagesList"]').click()
    browser.element('[data-value="5"]').click()
    browser.element('#select-package').click()
    browser.element('[value="Рассчитать"]').click()

    browser.element('.end-information1__price').should(have.text('516 '))