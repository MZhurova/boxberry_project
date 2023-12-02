import allure
from selene.support.shared import browser
from selene import have

from boxberry_tests.pages.parcel_info_page import ParcelInfoPage


def test_calculate_parcel_retail_client(setup_browser):
    parcel_info_page = ParcelInfoPage()
    parcel_info_page.open()
    browser.element('.cta__button').click()
    browser.element('[name="sender"]').type('Екатеринбург (Свердловская)')
    browser.element('[name="receiver"]').type('Томск (Томская)')
    browser.element('[name="publicPrice"]').type('0')
    browser.element('[data-handler="renderPackagesList"]').click()
    browser.element('[data-value="5"]').click()
    browser.element('#select-package').click()
    browser.element('[value="Рассчитать"]').click()

    browser.element('.end-information1__price').should(have.text('516 '))

def test_dd(setup_browser):
    parcel_info_page = ParcelInfoPage()
    parcel_info_page.open()
    browser.driver.execute_script("window.scrollTo(0, 1080)")
    browser.element('div.col-12.col-sm-auto  > .cta__button').click()

    browser.element('.pageTitle__title').should(have.text('Получить посылку'))