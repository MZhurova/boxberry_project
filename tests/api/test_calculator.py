import allure
import jsonschema
from boxberry_project_tests.utils.attach import load_schema, boxberry_api_get
from allure_commons.types import Severity


@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "m.zhurova")
@allure.label('layer', 'API')
@allure.title("Calculator api successfully")
@allure.feature("Calculate parcel")
def test_calculator_successfully(api_url):
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


@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "m.zhurova")
@allure.label('layer', 'API')
@allure.title("Calculator api successfully body")
@allure.feature("Calculate parcel")
def test_calculator_match_body(api_url):
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
        assert result.status_code == 200
        assert result.json() == file


@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "m.zhurova")
@allure.label('layer', 'API')
@allure.title("Calculator services cost")
@allure.feature("Calculate parcel")
def test_calculator_services_cost(api_url):
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
    schema = load_schema("response_calculate.json")

    with allure.step('Make a request'):
        result = boxberry_api_get(url=url)

    with allure.step('Assert the result'):
        assert result.status_code == 200
        jsonschema.validate(result.json(), schema)
        assert result.json()["status"] == 1
        assert result.json()["data"][0]["default_services_cost"] == 52450


@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "m.zhurova")
@allure.label('layer', 'API')
@allure.title("Calculator bad request")
@allure.feature("Calculate parcel")
def test_calculator_bad_request(api_url):
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
        assert result.json()["error"] is True
