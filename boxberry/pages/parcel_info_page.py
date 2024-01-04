from selene.support.shared import browser
from selene import have

class ParcelInfoPage:

    def open(self):
        browser.open('castnym-klientam/dostavka/otpravit_posylku')
        browser.element('.modal-new-year__btn_cancel').click()

    def calculate_parcel(self, city_start, city_finish):
        browser.element('.cta__button').click()
        browser.element('[name="sender"]').type(city_start)
        browser.element('[name="receiver"]').type(city_finish)
        browser.element('[name="publicPrice"]').type('0')
        browser.element('[data-handler="renderPackagesList"]').click()
        browser.element('[data-value="5"]').click()
        browser.element('#select-package').click()
        browser.element('[value="Рассчитать"]').click()

    def delivery_cost(self, value):
        browser.element('.end-information1__price').should(have.text(value))

    def click_how_receive_parsel(self):
        browser.driver.execute_script("window.scrollTo(0, 1080)")
        browser.element('div.col-12.col-sm-auto  > .cta__button').click()

    def assert_text_on_page_how_receive_parsel(self):
        browser.element('.pageTitle__title').should(have.text('Получить посылку'))
