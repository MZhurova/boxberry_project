import jsonschema
import requests
from utils.attach import load_schema
import json
import logging
import allure
from allure_commons._allure import step
from allure_commons.types import AttachmentType


def boxberry_api_get(url, **kwargs):
    with step("API Request"):
        result = requests.get(f'{url}', **kwargs)

        allure.attach(body=result.request.url, name="Request url",
                      attachment_type=AttachmentType.TEXT)
        allure.attach(body=json.dumps(result.request.body, indent=4, ensure_ascii=True), name="Request body",
                      attachment_type=AttachmentType.JSON, extension="json")
        allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=False), name="Response",
                      attachment_type=AttachmentType.JSON, extension="json")

        logging.info("Request: " + result.request.url)
        if result.request.body:
            logging.info("INFO Request body: " + result.request.body)
        logging.info("Request headers: " + str(result.request.headers))
        logging.info("Response code " + str(result.status_code))
        logging.info("Response: " + result.text)
    return result


def test_get_list_country_and_city(api_url):
    url = f'{api_url}/api/v1/cities/list'

    result = boxberry_api_get(f'{url}')

    assert result.status_code == 200
    assert result.json()["country"][0]["name"] == "Россия" and result.json()["country"][0]["code"] == "643"
    assert len(result.json()["country"][0]) == 12
    assert len(result.json()["country"]) == 7
    assert result.json()['cities'][0]["name"] == "Абакан" and result.json()['cities'][0]["code"] == "5"
    assert len(result.json()["cities"]) == 912


def test_get_daily(api_url):
    url = f'{api_url}/api/v1/cbr/daily'
    schema = load_schema("response_daily.json")

    result = boxberry_api_get(f'{url}',
                              headers={'Cookie': 'sticky_cookie=http://boxberry-app-1.ru-central1.internal'})

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert len(result.json()[0]) == 5


def test_get_city(api_url):
    cityCode = 57
    perPage = 10
    url = f'{api_url}/api/v1/odp?'
    schema = load_schema("response_city.json")

    result = boxberry_api_get(
        url=url,
        params={"cityCode": cityCode, "perPage": perPage}
    )

    assert result.status_code == 200
    assert result.json()["odp"][0]["cityCode"] == str(cityCode)
    assert len(result.json()['odp']) == perPage
    jsonschema.validate(result.json(), schema)


def test_get_tracking(api_url):
    searchId = 'ACND280139442'
    url = f'{api_url}/api/v1/tracking/order/get'
    schema = load_schema("response_tracking.json")

    result = boxberry_api_get(
        url=url,
        params={"searchId": searchId}
    )

    assert result.status_code == 200
    assert result.json()[0]["ProgramNumber"] == searchId
    jsonschema.validate(result.json(), schema)


def test_get_tracking_not_faund(api_url):
    searchId = 'fffftttttttttttt'
    url = f'{api_url}/api/v1/tracking/order/get'

    result = boxberry_api_get(
        url=url,
        params={"searchId": searchId}
    )

    assert result.status_code == 200
    assert result.json() == []


def test_get_calculator(api_url):
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
    schema = load_schema("response_calculate.json")
    file = load_schema("rrr.json")
    result = boxberry_api_get(url=url)

    assert result.status_code == 200
    assert result.json()["status"] == 1
    assert result.json()["data"][0]["default_services_cost"] == 56300
    jsonschema.validate(result.json(), schema)
    print("///////////////")
    print(result.json())
    print("///////////////")
    print(file)
    print("///////////////")
    assert result.json() == file
