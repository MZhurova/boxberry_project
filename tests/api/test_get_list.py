import jsonschema
import requests
from requests import Response
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
        allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True), name="Response",
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
    assert result.json()["country"][0]["name"] == "Россия"


def test_get_daily(api_url):
    url = f'{api_url}/api/v1/cbr/daily'
    schema = load_schema("response_daily.json")

    result = boxberry_api_get(f'{url}')

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)


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
    logging.info(result.request.url)
    logging.info(result.status_code)
    logging.info(result.text)
    logging.info(result.request.body)

    print(result.request.body)
    print(result.text)



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


