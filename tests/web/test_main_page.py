from boxberry_project_tests.pages.main_page import main_page
import allure
from allure_commons.types import Severity


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "mzhurova")
@allure.label('layer', 'WEB')
@allure.title("Set city")
@allure.feature("City")
def test_set_city(setup_browser):
    with allure.step('Open main page'):
        main_page.open()
    with allure.step('Select city'):
        main_page.select_city('Томск')

    with allure.step("Assert chosen city"):
        main_page.assert_city('Томск')


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "mzhurova")
@allure.label('layer', 'WEB')
@allure.title("Open page login im")
@allure.feature("Login IM")
def test_open_page_login_im(setup_browser):
    with allure.step('Open main page'):
        main_page.open()
    with allure.step('Verification city'):
        main_page.verification_city()
    with allure.step('View the list of personal account'):
        main_page.view_list_personal_account()
    with allure.step('Choosing a personal account for online stores'):
        main_page.choose_im()

    with allure.step('Assert chosen personal account'):
        main_page.assert_personal_account()


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "mzhurova")
@allure.label('layer', 'WEB')
@allure.title("Recovery password for im")
@allure.feature("Password recovery")
def test_recovery_password_im(setup_browser):
    with allure.step('Open the login page for online stores'):
        main_page.open_page_im()
    with allure.step('Input login'):
        main_page.input_login_im()
    with allure.step('Clicking "forgot password"'):
        main_page.forgot_password()

    with allure.step('Assert open page "Password recovery"'):
        main_page.assert_open_page_password_recovery()


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "mzhurova")
@allure.label('layer', 'WEB')
@allure.title("Parsel search")
@allure.feature("Tracking")
def test_parcel_search(setup_browser):
    with allure.step('Open main page'):
        main_page.open()
    with allure.step('Parsel tracking'):
        main_page.parsel_tracking('ACND280139442')

    with allure.step('Assert status parcel'):
        main_page.status_parcel()
