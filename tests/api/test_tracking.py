import allure
import jsonschema
from boxberry_project_tests.utils.attach import load_schema, boxberry_api_get
from allure_commons.types import Severity


@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "mzhurova")
@allure.label('layer', 'API')
@allure.title("Tracking api successfully")
@allure.feature("Tracking")
def test_tracking_successfully(api_url):
    search_id = '5555'
    url = f'{api_url}/api/v1/tracking/order/get'
    schema = load_schema("response_tracking.json")

    with allure.step('Make a request'):
        result = boxberry_api_get(
            url=url,
            params={"searchId": search_id}
        )

    with allure.step('Assert the result'):
        assert result.status_code == 200
        jsonschema.validate(result.json(), schema)


@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "mzhurova")
@allure.label('layer', 'API')
@allure.title("Tracking faund by searchid")
@allure.feature("Tracking")
def test_tracking_faund_searchid(api_url):
    search_id = 'ACND280139442'
    url = f'{api_url}/api/v1/tracking/order/get'
    schema = load_schema("response_tracking.json")

    with allure.step('Make a request'):
        result = boxberry_api_get(
            url=url,
            params={"searchId": search_id}
        )

    with allure.step('Assert the result'):
        assert result.status_code == 200
        jsonschema.validate(result.json(), schema)
        assert result.json()[0]["ProgramNumber"] == search_id


@allure.tag("api")
@allure.severity(Severity.MINOR)
@allure.label("owner", "mzhurova")
@allure.label('layer', 'API')
@allure.title("Tracking not found")
@allure.feature("Tracking")
def test_tracking_not_found(api_url):
    search_id = 'fffftttttttttttt'
    url = f'{api_url}/api/v1/tracking/order/get'
    schema = load_schema("response_tracking.json")

    with allure.step('Make a request'):
        result = boxberry_api_get(
            url=url,
            params={"searchId": search_id}
        )

    with allure.step('Assert the result'):
        assert result.status_code == 200
        jsonschema.validate(result.json(), schema)
        assert result.json() == []
