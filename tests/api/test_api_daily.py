import allure
import jsonschema
from utils.attach import load_schema, boxberry_api_get


def test_api_daily_successfully(api_url):
    url = f'{api_url}/api/v1/cbr/daily'
    schema = load_schema("response_daily.json")

    with allure.step('Make a request'):
        result = boxberry_api_get(f'{url}',
                              headers={'Cookie': 'sticky_cookie=http://boxberry-app-1.ru-central1.internal'})

    with allure.step('Assert the result'):
        assert result.status_code == 200
        jsonschema.validate(result.json(), schema)



def test_api_daily_match_body(api_url):
    url = f'{api_url}/api/v1/cbr/daily'
    file = load_schema("daily_body.json")

    with allure.step('Make a request'):
        result = boxberry_api_get(f'{url}',
                                  headers={'Cookie': 'sticky_cookie=http://boxberry-app-1.ru-central1.internal'})

    with allure.step('Assert the result'):
        assert len(result.json()[0]) == 5
        assert file == result.json()


