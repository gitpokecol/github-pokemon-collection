from unittest.mock import MagicMock

import pytest
from httpx import Response

from src.external.ip_api import IpAPI
from tests.utils.common import mock_coroutine


@pytest.fixture(scope="session")
def mock_client():
    return MagicMock()


@pytest.fixture
def ip_api(mock_client: MagicMock):
    ip_api = IpAPI()
    ip_api.client = mock_client
    return ip_api


async def test_get_timezone_by_ip_address__response_400_status_code__return_None(
    ip_api: IpAPI, mock_client: MagicMock
):
    # given
    any_ip_address = "8.8.8.8"
    mock_client.get = mock_coroutine(Response(400))

    # when
    result = await ip_api.get_timezone_by_ip_address(any_ip_address)

    # then
    assert result is None


async def test_get_timezone_by_ip_address__response_success_status__return_IpApiResponse(
    ip_api: IpAPI, mock_client: MagicMock
):
    # given
    any_ip_address = "8.8.8.8"
    res_json = {"status": "success", "timezone": "Asia/Seoul"}
    mock_client.get = mock_coroutine(Response(200, json=res_json))

    # when
    result = await ip_api.get_timezone_by_ip_address(any_ip_address)

    # then
    assert result is not None
    assert result.status == res_json["status"]
    assert result.timezone == res_json["timezone"]


async def test_get_timezone_by_ip_address__response_fail_status__return_IpApiResponse(
    ip_api: IpAPI, mock_client: MagicMock
):
    # given
    any_ip_address = "8.8.8.8"
    res_json = {"status": "fail", "message": "it was not cool acting bro!", "query": "8.8.8.8"}
    mock_client.get = mock_coroutine(Response(200, json=res_json))

    # when
    result = await ip_api.get_timezone_by_ip_address(any_ip_address)

    # then
    assert result is not None
    assert result.status == "fail"
    assert result.timezone is None
