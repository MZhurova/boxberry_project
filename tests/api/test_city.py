import allure
import jsonschema
import pytest
from boxberry_project_tests.utils.attach import load_schema, boxberry_api_get
from allure_commons.types import Severity


@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "m.zhurova")
@allure.label('layer', 'API')
@allure.title("City api successfully")
@allure.feature("City")
def test_city_successfully(api_url):
    city_code = 57
    url = f'{api_url}/api/v1/odp?'
    schema = load_schema("response_city.json")

    with allure.step('Make a request'):
        result = boxberry_api_get(
            url=url,
            params={"cityCode": city_code}
        )

    with allure.step('Assert the result'):
        assert result.status_code == 200
        jsonschema.validate(result.json(), schema)


@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "m.zhurova")
@allure.label('layer', 'API')
@allure.title("City found by citycode and perpage")
@allure.feature("City")
def test_citycode_and_perpage(api_url):
    city_code = 57
    per_page = 10
    url = f'{api_url}/api/v1/odp?'

    with allure.step('Make a request'):
        result = boxberry_api_get(
            url=url,
            params={"cityCode": city_code, "perPage": per_page}
        )
        schema = load_schema("response_city.json")

    with allure.step('Assert the result'):
        assert result.status_code == 200
        jsonschema.validate(result.json(), schema)
        assert result.json()["odp"][0]["cityCode"] == str(city_code)
        assert len(result.json()['odp']) == per_page


@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "m.zhurova")
@allure.label('layer', 'API')
@allure.title("City found by citycode")
@allure.feature("City")
@pytest.mark.parametrize('city_code', [57, 19, 22, 44])
def test_city_parametrize(api_url, city_code):
    url = f'{api_url}/api/v1/odp?'

    with allure.step('Make a request'):
        result = boxberry_api_get(
            url=url,
            params={"cityCode": city_code}
        )

    with allure.step('Assert the result'):
        assert result.status_code == 200
        assert result.json()["odp"][0]["cityCode"] == str(city_code)
