import allure
from boxberry_project_tests.pages.parcel_info_page import parcel_info_page
from allure_commons.types import Severity


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "mzhurova")
@allure.label('layer', 'WEB')
@allure.title("Calculate parcel retail client")
@allure.feature("Calculate parcel")
def test_calculate_parcel_retail_client(setup_browser):
    with allure.step('Open parcel information page'):
        parcel_info_page.open()
    with allure.step('Calculate the cost of the parcel'):
        parcel_info_page.calculate_parcel('Екатеринбург (Свердловская)', 'Томск (Томская)')

    with allure.step('Assert delivery cost'):
        parcel_info_page.delivery_cost('522 ')


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "mzhurova")
@allure.label('layer', 'WEB')
@allure.title("Parcel information page")
@allure.feature("Parcel info")
def test_info_how_receive_parsel(setup_browser):
    with allure.step('Open parcel information page'):
        parcel_info_page.open()
    with allure.step('Click on the "how to receive a parcel" button'):
        parcel_info_page.click_how_receive_parsel()

    with allure.step('Assert description of how to receive the parcel'):
        parcel_info_page.assert_text_on_page_how_receive_parsel()
