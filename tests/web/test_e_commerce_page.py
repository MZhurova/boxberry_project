from boxberry_project_tests.pages.e_commerce_page import e_commerce_page
import allure
from allure_commons.types import Severity


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "mzhurova")
@allure.label('layer', 'WEB')
@allure.title("Calculate parcel business client")
@allure.feature("Calculate parcel")
def test_calculate_parcel_business_client(setup_browser):
    with allure.step('Open e-commerce page'):
        e_commerce_page.open()
    with allure.step('Calculate the cost of the parcel for business partner'):
        e_commerce_page.calculate_parcel_for_business('Екатеринбург', 'Томск', '5', '6', '7', '11')

    with allure.step('Assert delivery cost for business partner'):
        e_commerce_page.delivery_cost_for_business('1 568')


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "mzhurova")
@allure.label('layer', 'WEB')
@allure.title("Show point")
@allure.feature("Points")
def test_show_point(setup_browser):
    with allure.step('Open e-commerce page'):
        e_commerce_page.open()
    with allure.step('Clicking the button show point'):
        e_commerce_page.click_show_point()
    with allure.step('Set the city to view point'):
        e_commerce_page.set_city_to_view_point()

    with allure.step("Assert chosen city"):
        e_commerce_page.assert_chosen_city('Новосибирск')


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "mzhurova")
@allure.label('layer', 'WEB')
@allure.title("Parcel not found")
@allure.feature("Tracking")
def test_parcel_not_found(setup_browser):
    with allure.step('Open e-commerce page'):
        e_commerce_page.open()
    with allure.step('Parsel tracking'):
        e_commerce_page.parsel_no_vaild_tracking('5546456565645')

    with allure.step('Assert parcel not found'):
        e_commerce_page.assert_parcel_not_found()
