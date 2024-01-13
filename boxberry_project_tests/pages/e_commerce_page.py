from selene import browser, have, be, command


class ECommercePage:

    def open(self):
        browser.open('e-commerce')
        browser.element('.modal-new-year__btn_cancel').click()

    def calculate_parcel_for_business(self, start_city, finish_city, height, length, width, weight):
        browser.element('#item-calculator > a').click()
        browser.element('.scheme__icon').perform(command.js.scroll_into_view)
        browser.element('.calculator__head').should(be.visible).click()
        browser.element('.multiselect__placeholder').click()
        browser.element('input.multiselect__input').should(be.blank).type(start_city).press_enter()
        browser.element('.multiselect__placeholder').click()
        browser.element('[placeholder="Город-получатель"]').should(be.blank).type(finish_city).press_enter()
        browser.element('#calcCost').type('0')
        browser.element('#calcHeight').type(height)
        browser.element('#calcWidth').type(length)
        browser.element('#calcLength').type(width)
        browser.element('#calcWeight').type(weight)
        browser.element('#calculator > ul > div:nth-child(2) > div > a.calculator__button').click()
        browser.element('.calculator-total__cost').should(have.text('1 568'))

    def delivery_cost_for_business(self, value):
        browser.element('.calculator-total__cost').should(have.text(value))

    def click_show_point(self):
        browser.element('#item-map-send > a.button.button_red').click()

    def set_city_to_view_point(self):
        browser.element('.city-name').click()
        browser.element('.town-popup__list-wrap li:nth-child(4)').click()

    def assert_chosen_city(self, chosen_city):
        browser.element('.city-name').should(have.text(chosen_city))

    def parsel_no_vaild_tracking(self, no_valid_nomber_parsel):
        browser.element('[placeholder="Трек-номер"]').type(no_valid_nomber_parsel)
        browser.element('button.button').click()

    def assert_parcel_not_found(self):
        browser.element('.empty-search-result__title').should(have.text('Номер заказа не найден'))


e_commerce_page = ECommercePage()
