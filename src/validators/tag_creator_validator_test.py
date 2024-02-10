import pytest
from .tag_creator_validator import tag_creator_validator


class MockRequest:
    def __init__(self, json):
        self.json = json


def test_tag_creator_validator():
    req = MockRequest(
        json={
            "product_code": "test1234",
        }
    )
    tag_creator_validator(req)


def test_tag_creator_validator_fail():
    req = MockRequest(
        json={
            "product_code": "test1234",
            "product_name": "test1234",
            "product": 1234,
        }
    )
    with pytest.raises(Exception):
        tag_creator_validator(req)
