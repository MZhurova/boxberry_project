import allure
from utils.attach import load_schema, boxberry_api_get


def test_api_list_country_and_city_successfully(api_url):
    url = f'{api_url}/api/v1/cities/list'
    file = load_schema("country_and_city_body.json")

    with allure.step('Make a request'):
        result = boxberry_api_get(f'{url}')

    with allure.step('Assert the result'):
        assert result.status_code == 200
        assert file == result.json()


def test_api_list_country_name_code_and_len(api_url):
    url = f'{api_url}/api/v1/cities/list'

    with allure.step('Make a request'):
        result = boxberry_api_get(f'{url}')

    with allure.step('Assert the result'):
        assert result.status_code == 200
        assert result.json()["country"][0]["name"] == "Россия" and result.json()["country"][0]["code"] == "643"
        assert len(result.json()["country"][0]) == 12
        assert len(result.json()["country"]) == 7


def test_api_list_city_name_code_and_len(api_url):
    url = f'{api_url}/api/v1/cities/list'

    with allure.step('Make a request'):
        result = boxberry_api_get(f'{url}')

    with allure.step('Assert the result'):
        assert result.json()['cities'][0]["name"] == "Абакан" and result.json()['cities'][0]["code"] == "5"
        assert len(result.json()["cities"]) == 911


