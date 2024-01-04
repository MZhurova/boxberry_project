import allure
from boxberry.pages.parcel_info_page import ParcelInfoPage


def test_calculate_parcel_retail_client(setup_browser):
    parcel_info_page = ParcelInfoPage()
    with allure.step('Open parcel information page'):
        parcel_info_page.open()
    with allure.step('Calculate the cost of the parcel'):
        parcel_info_page.calculate_parcel('Екатеринбург (Свердловская)','Томск (Томская)')

    with allure.step('Assert delivery cost'):
        parcel_info_page.delivery_cost('516 ')


def test_info_how_receive_parsel(setup_browser):
    parcel_info_page = ParcelInfoPage()
    with allure.step('Open parcel information page'):
        parcel_info_page.open()
    with allure.step('Click on the "how to receive a parcel" button'):
        parcel_info_page.click_how_receive_parsel()

    with allure.step('Assert description of how to receive the parcel'):
        parcel_info_page.assert_text_on_page_how_receive_parsel()
