from selene.support.shared import browser
from selene import have, command
import time



class ECommercePage:

    def open(self):
        browser.open('e-commerce')

    def calculate_parcel_for_business(self, start_city, finish_city, height, length, width, weight):
        browser.element('a.button.button_red').click()
        browser.element('.multiselect__placeholder').click()
        time.sleep(3)
        browser.element('input.multiselect__input').type(start_city).press_enter()
        browser.element('.multiselect__placeholder').click()
        time.sleep(3)
        browser.element('[placeholder="Город-получатель"]').type(finish_city).press_enter()
        browser.element('[placeholder="Оценочная стоимость"]').type('0')
        browser.element('[placeholder="Высота"]').type(height)
        browser.element('[placeholder="Ширина"]').type(length)
        browser.element('[placeholder="Длина"]').type(width)
        browser.element('#calcWeight').type(weight)
    #   browser.element('div[class="calculator-nav__inner"] a:nth-child(2)').click()

    def delivery_cost_for_business(self, value):
    #    browser.element('.calculator-total__cost').should(have.text(value))
        pass

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