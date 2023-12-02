import time

from boxberry_tests.pages.e_commerce_page import ECommercePage
import allure
from selene.support.shared import browser
from selene import have, by


def test_calculate_parcel_business_client(setup_browser):
    e_commerce_page = ECommercePage()
    with allure.step('Open e-commerce page'):
        e_commerce_page.open()
    with allure.step('Calculate the cost of the parcel for business partner'):
        e_commerce_page.calculate_parcel_for_business('Екатеринбург', 'Томск', '5', '6', '7', '11')

    with allure.step('Assert delivery cost for business partner'):
        pass
    #   e_commerce_page.delivery_cost_for_business('1 568')


def test_show_point(setup_browser):
    e_commerce_page = ECommercePage()
    with allure.step('Open e-commerce page'):
        e_commerce_page.open()
    with allure.step('Clicking the button show point'):
        e_commerce_page.click_show_point()
    with allure.step('Set the city to view point'):
        e_commerce_page.set_city_to_view_point()

    with allure.step("Assert chosen city"):
        e_commerce_page.assert_chosen_city('Новосибирск')


def test_parcel_not_found(setup_browser):
    e_commerce_page = ECommercePage()
    with allure.step('Open e-commerce page'):
        e_commerce_page.open()
    with allure.step('Parsel tracking'):
        e_commerce_page.parsel_no_vaild_tracking('5546456565645')

    with allure.step('Assert parcel not found"'):
        e_commerce_page.assert_parcel_not_found()



