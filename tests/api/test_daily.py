import allure
import jsonschema
from boxberry_project_tests.utils.attach import load_schema, boxberry_api_get
from allure_commons.types import Severity


@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "mzhurova")
@allure.label('layer', 'API')
@allure.title("Daily api successfull")
@allure.feature("Daily")
def test_daily_successfully(api_url):
    url = f'{api_url}/api/v1/cbr/daily'
    schema = load_schema("response_daily.json")

    with allure.step('Make a request'):
        result = boxberry_api_get(f'{url}',
                                  headers={'Cookie': 'sticky_cookie=http://boxberry-app-1.ru-central1.internal'})

    with allure.step('Assert the result'):
        assert result.status_code == 200
        jsonschema.validate(result.json(), schema)


@allure.tag("api")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "mzhurova")
@allure.label('layer', 'API')
@allure.title("Daily api successfull body and len")
@allure.feature("Daily")
def test_daily_match_body(api_url):
    url = f'{api_url}/api/v1/cbr/daily'
    file = load_schema("daily_body.json")
    schema = load_schema("response_daily.json")

    with allure.step('Make a request'):
        result = boxberry_api_get(f'{url}',
                                  headers={'Cookie': 'sticky_cookie=http://boxberry-app-1.ru-central1.internal'})

    with allure.step('Assert the result'):
        assert result.status_code == 200
        jsonschema.validate(result.json(), schema)
        assert len(result.json()[0]) == 5
        assert file == result.json()
