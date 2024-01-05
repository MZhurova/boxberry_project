import allure
import jsonschema
import pytest
from utils.attach import load_schema, boxberry_api_get


def test_api_city_successfully(api_url):
    cityCode = 57
    url = f'{api_url}/api/v1/odp?'
    schema = load_schema("response_city.json")

    with allure.step('Make a request'):
        result = boxberry_api_get(
            url=url,
            params={"cityCode": cityCode}
        )

    with allure.step('Assert the result'):
        assert result.status_code == 200
        jsonschema.validate(result.json(), schema)


def test_api_citycode_and_perpage(api_url):
    cityCode = 57
    perPage = 10
    url = f'{api_url}/api/v1/odp?'

    with allure.step('Make a request'):
        result = boxberry_api_get(
            url=url,
            params={"cityCode": cityCode, "perPage": perPage}
        )

    with allure.step('Assert the result'):
        assert result.json()["odp"][0]["cityCode"] == str(cityCode)
        assert len(result.json()['odp']) == perPage


@pytest.mark.parametrize('cityCode', [57, 19, 22, 44])
def test_api_city_parametrize(api_url, cityCode):
    url = f'{api_url}/api/v1/odp?'

    with allure.step('Make a request'):
        result = boxberry_api_get(
            url=url,
            params={"cityCode": cityCode}
        )

    with allure.step('Assert the result'):
        assert result.json()["odp"][0]["cityCode"] == str(cityCode)