import allure
import jsonschema
from utils.attach import load_schema, boxberry_api_get


def test_tracking_successfully(api_url):
    searchId = '5555'
    url = f'{api_url}/api/v1/tracking/order/get'
    schema = load_schema("response_tracking.json")

    with allure.step('Make a request'):
        result = boxberry_api_get(
            url=url,
            params={"searchId": searchId}
        )

    with allure.step('Assert the result'):
        assert result.status_code == 200
        jsonschema.validate(result.json(), schema)


def test_tracking_faund_searchid(api_url):
    searchId = 'ACND280139442'
    url = f'{api_url}/api/v1/tracking/order/get'
    schema = load_schema("response_tracking.json")

    with allure.step('Make a request'):
        result = boxberry_api_get(
            url=url,
            params={"searchId": searchId}
        )

    with allure.step('Assert the result'):
        assert result.status_code == 200
        jsonschema.validate(result.json(), schema)
        assert result.json()[0]["ProgramNumber"] == searchId


def test_tracking_not_found(api_url):
    searchId = 'fffftttttttttttt'
    url = f'{api_url}/api/v1/tracking/order/get'
    schema = load_schema("response_tracking.json")

    with allure.step('Make a request'):
        result = boxberry_api_get(
            url=url,
            params={"searchId": searchId}
        )

    with allure.step('Assert the result'):
        assert result.status_code == 200
        jsonschema.validate(result.json(), schema)
        assert result.json() == []
