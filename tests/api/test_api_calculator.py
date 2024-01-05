import allure
import jsonschema
from utils.attach import load_schema, boxberry_api_get


def test_api_calculator_successfully(api_url):
    method = "TarificationLaP"
    sender_city = 23
    receiver_city = 19
    public_price = 100000
    url = (f'{api_url}/proxy/delivery/cost/pip?'
           f'method={method}'
           f'&sender_city={sender_city}'
           f'&receiver_city={receiver_city}'
           f'&public_price={public_price}'
           f'&package[boxberry_package]='
           f'&package[width]=2'
           f'&package[height]=2&'
           f'package[depth]=2'
           )
    schema = load_schema("response_calculate.json")

    with allure.step('Make a request'):
        result = boxberry_api_get(url=url)

    with allure.step('Assert the result'):
        assert result.status_code == 200
        jsonschema.validate(result.json(), schema)


def test_api_calculator_match_body(api_url):
    method = "TarificationLaP"
    sender_city = 25
    receiver_city = 57
    public_price = 100000
    url = (f'{api_url}/proxy/delivery/cost/pip?'
           f'method={method}'
           f'&sender_city={sender_city}'
           f'&receiver_city={receiver_city}'
           f'&public_price={public_price}'
           f'&package[boxberry_package]='
           f'&package[width]=2'
           f'&package[height]=2&'
           f'package[depth]=2'
           )
    file = load_schema("calculate_body.json")

    with allure.step('Make a request'):
        result = boxberry_api_get(url=url)

    with allure.step('Assert the result'):
        assert result.json() == file


def test_api_calculator_services_cost(api_url):
    method = "TarificationLaP"
    sender_city = 11
    receiver_city = 41
    public_price = 250000
    url = (f'{api_url}/proxy/delivery/cost/pip?'
           f'method={method}'
           f'&sender_city={sender_city}'
           f'&receiver_city={receiver_city}'
           f'&public_price={public_price}'
           f'&package[boxberry_package]='
           f'&package[width]=2'
           f'&package[height]=2&'
           f'package[depth]=2'
           )

    with allure.step('Make a request'):
        result = boxberry_api_get(url=url)

    with allure.step('Assert the result'):
        assert result.json()["status"] == 1
        assert result.json()["data"][0]["default_services_cost"] == 51850


def test_api_calculator_bad_request(api_url):
    method = "TarificationLaP"
    sender_city = ""
    receiver_city = ""
    public_price = 2500
    url = (f'{api_url}/proxy/delivery/cost/pip?'
           f'method={method}'
           f'&sender_city={sender_city}'
           f'&receiver_city={receiver_city}'
           f'&public_price={public_price}'
           f'&package[boxberry_package]='
           f'&package[width]=2'
           f'&package[height]=2&'
           f'package[depth]=2'
           )
    schema = load_schema("response_calculate_bad_request.json")

    with allure.step('Make a request'):
        result = boxberry_api_get(url=url)

    with allure.step('Assert the result'):
        assert result.status_code == 400
        jsonschema.validate(result.json(), schema)
        assert result.json()["error"] == True