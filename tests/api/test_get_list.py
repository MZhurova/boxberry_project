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

    # result: Response = requests.get(url)
    result = boxberry_api_get(f'{url}')
    assert result.status_code == 200

    # with step("API Request"):
    #     result = requests.get(url)
    #     allure.attach(body=result.request.url, name="Request url",
    #                   attachment_type=AttachmentType.TEXT)
    #     allure.attach(body=json.dumps(result.request.body, indent=4, ensure_ascii=True), name="Request body",
    #                   attachment_type=AttachmentType.JSON, extension="json")
    #     allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True), name="Response",
    #                   attachment_type=AttachmentType.JSON, extension="json")
    #     logging.info(result.request.url)
    #     logging.info(result.status_code)
    #     logging.info(result.text)


def test_get_daily(api_url):
    url = f'{api_url}/api/v1/cbr/daily'
    schema = load_schema("response_daily.json")

    # result: Response = requests.get(url)
    result = boxberry_api_get(f'{url}')
    assert result.status_code == 200

    jsonschema.validate(result.json(), schema)

    # with step("API Request"):
    #     result = requests.get(url)
    #     allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True), name="Response",
    #                   attachment_type=AttachmentType.JSON, extension="json")
    #     logging.info(result.request.url)
    #     logging.info(result.status_code)
    #     logging.info(result.text)


def test_get_city(api_url):
    cityCode = 57
    perPage = 10
    url = f'{api_url}/api/v1/odp?'
    schema = load_schema("response_city.json")

    result = boxberry_api_get(
        url=url,
        params={"cityCode": cityCode, "perPage": perPage}
    )
    # result = requests.get(
    #     url=url,
    #     params={"cityCode": cityCode, "perPage": perPage}
    # )
    assert result.status_code == 200
    # assert result.json()['cityCode'] == cityCode
    jsonschema.validate(result.json(), schema)
    # assert result.json()["perPage"] == perPage
    # assert len(result.json()['odp']) == perPage
    logging.info(result.request.url)
    logging.info(result.status_code)
    logging.info(result.text)
    logging.info(result.request.body)

    print(result.request.body)
    print(result.text)


def test_get_city2(api_url):
    url = f'{api_url}/api/v1/odp?cityCode=57&perPage=10'
    schema = load_schema("response_city.json")

    result = requests.get(url)
    assert result.status_code == 200
    # assert result.json()['cityCode'] == '57'
    jsonschema.validate(result.json(), schema)
    # assert result.json()["perPage"] == perPage
    # assert len(result.json()['odp']) == perPage
    logging.info(result.request.url)
    logging.info(result.status_code)
    logging.info(result.text)

    print(result.text)
