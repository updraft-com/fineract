from datetime import date, datetime

import pytest
import pytz

from conftest import find_in_reference_configuration
import factory
from datetime import datetime


def test_connect_to_fineract(mifos_client):
    r = mifos_client.request("get", "/configurations")

    assert r.status_code == 200
    for config in r.json()["globalConfiguration"]:
        assert config == find_in_reference_configuration(config["name"])


def test_check_loan_configuration(mifos_client):
    r = mifos_client.request("get", "/loanproducts")
    assert r.status_code == 200
    ql1 = None
    for product in r.json():
        if product["shortName"] == "ql1":
            ql1 = product
            break
    assert ql1


def test_create_client(mifos_client):
    r = mifos_client.request("post", "/clients", json=factory.create_client())
    assert r.status_code == 200
    assert "clientId" in r.json()


