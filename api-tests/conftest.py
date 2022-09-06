from datetime import date

import pytest
import requests
from requests.auth import HTTPBasicAuth

import fineract_configuration


class MifosAPIClient:
    def __init__(self, username=None, password=None, base_url=None):
        self.username = username
        self.password = password
        self.base_url = base_url

        self._session = None

    def _get_session(self) -> requests.Session:
        """
        Get a requests Session that will include the appropriate Authorization
        header for the authorization details provided to this MifosAPIClient.
        We cache and re-use the same sesssion for the lifetime of the
        MifosAPIClient instance to potentially gain benefits from TCP socket
        re-use etc.
        """
        if not self._session:
            self._session = requests.Session()
            self._session.auth = HTTPBasicAuth(self.username, self.password)
            self._session.headers = {"Fineract-Platform-TenantId": "default"}

        return self._session

    def request(self, method, url, *args, **kwargs) -> requests.Response:
        """
        Send a raw HTTP request using this client's Session instance. The
        request will automatically include an authentication header containing
        a the credentials provided when initialzing this instance.

        This method is primarily intended for use by higher-level methods that
        call specific endpoints and should be avoided in general use.
        Forwards all positional and keyword arguments onto the underlying
        Session's `request()` method.
        """
        return self._get_session().request(
            method, f"{self.base_url}{url}", *args, **kwargs
        )


@pytest.fixture(autouse=True)
def mifos_client():
    MIFOS_API_URL = "https://localhost:8443/fineract-provider/api/v1"
    MIFOS_USERNAME = "mifos"
    MIFOS_PASSWORD = "password"
    client = MifosAPIClient(
        username=MIFOS_USERNAME,
        password=MIFOS_PASSWORD,
        base_url=MIFOS_API_URL,
    )
    client._get_session().verify = False
    return client


def find_in_reference_configuration(param):
    for config in fineract_configuration.configurations["globalConfiguration"]:
        if config["name"] == param:
            return config
    return None


def global_configuration():
    r = requests.get(
        "https://localhost:8443/fineract-provider/api/v1/configurations",
        verify=False,
        auth=HTTPBasicAuth("mifos", "password"),
        headers={"Fineract-Platform-TenantId": "default"},
    )
    assert r.status_code == 200
    assert "globalConfiguration" in r.json()
    assert len(r.json()["globalConfiguration"]) >= 38
    for config in r.json()["globalConfiguration"]:
        ref_config = find_in_reference_configuration(config["name"])
        if ref_config["enabled"] != config["enabled"]:
            r = requests.put(
                f"https://localhost:8443/fineract-provider/api/v1/configurations/{config['id']}",
                verify=False,
                auth=HTTPBasicAuth("mifos", "password"),
                headers={"Fineract-Platform-TenantId": "default"},
                json={"enabled": ref_config["enabled"]},
            )
            assert r.status_code == 200
        if "stringValue" not in ref_config:
            if ref_config["value"] != config["value"]:
                r = requests.put(
                    f"https://localhost:8443/fineract-provider/api/v1/configurations/{config['id']}?resourceType=configurations",
                    verify=False,
                    auth=HTTPBasicAuth("mifos", "password"),
                    headers={"Fineract-Platform-TenantId": "default"},
                    json={"value": ref_config["value"]},
                )
                assert r.status_code == 200
        if "stringValue" in ref_config:
            if (
                ref_config["value"] != config["value"]
                or ref_config["stringValue"] != config["stringValue"]
            ):
                r = requests.put(
                    f"https://localhost:8443/fineract-provider/api/v1/configurations/{config['id']}?resourceType=configurations",
                    verify=False,
                    auth=HTTPBasicAuth("mifos", "password"),
                    headers={"Fineract-Platform-TenantId": "default"},
                    json={
                        "value": ref_config["value"],
                        "stringValue": ref_config["stringValue"],
                    },
                )
                assert r.status_code == 200


def office_configuration():
    r = requests.get(
        "https://localhost:8443/fineract-provider/api/v1/offices",
        verify=False,
        auth=HTTPBasicAuth("mifos", "password"),
        headers={"Fineract-Platform-TenantId": "default"},
    )
    assert r.status_code == 200
    assert len(r.json()) > 0


def holiday_configuration():
    # Configure statutory holidays
    holidays = [
        {
            "start": date(2019, 12, 25),
            "to": date(2019, 12, 27),
        },
        {
            "start": date(2019, 12, 26),
            "to": date(2019, 12, 27),
        },
        {
            "start": date(2019, 4, 19),
            "to": date(2019, 4, 23),
        },
        {
            "start": date(2019, 4, 22),
            "to": date(2019, 4, 23),
        },
        {
            "start": date(2019, 5, 27),
            "to": date(2019, 5, 28),
        },
        {
            "start": date(2019, 8, 26),
            "to": date(2019, 8, 27),
        },
        {
            "start": date(2020, 1, 1),
            "to": date(2020, 1, 2),
        },
        {
            "start": date(2020, 12, 25),
            "to": date(2020, 12, 29),
        },
        {
            "start": date(2020, 12, 26),
            "to": date(2020, 12, 29),
        },
        {
            "start": date(2020, 4, 10),
            "to": date(2020, 4, 14),
        },
        {
            "start": date(2020, 4, 13),
            "to": date(2020, 4, 14),
        },
        {
            "start": date(2020, 5, 25),
            "to": date(2020, 5, 26),
        },
        {
            "start": date(2020, 5, 8),
            "to": date(2020, 5, 11),
        },
        {
            "start": date(2020, 8, 31),
            "to": date(2020, 9, 1),
        },
        {
            "start": date(2021, 1, 1),
            "to": date(2021, 1, 4),
        },
        {
            "start": date(2021, 12, 27),
            "to": date(2021, 12, 29),
        },
        {
            "start": date(2021, 12, 28),
            "to": date(2021, 12, 29),
        },
        {
            "start": date(2021, 4, 2),
            "to": date(2021, 4, 6),
        },
        {
            "start": date(2021, 4, 5),
            "to": date(2021, 4, 6),
        },
        {
            "start": date(2021, 5, 3),
            "to": date(2021, 5, 4),
        },
        {
            "start": date(2021, 5, 31),
            "to": date(2021, 6, 1),
        },
        {
            "start": date(2021, 8, 30),
            "to": date(2021, 8, 31),
        },
        {
            "start": date(2022, 1, 2),
            "to": date(2022, 1, 3),
        },
        {
            "start": date(2022, 4, 15),
            "to": date(2022, 4, 19),
        },
        {
            "start": date(2022, 4, 18),
            "to": date(2022, 4, 19),
        },
        {
            "start": date(2022, 5, 2),
            "to": date(2022, 5, 3),
        },
        {
            "start": date(2022, 6, 2),
            "to": date(2022, 6, 6),
        },
        {
            "start": date(2022, 6, 3),
            "to": date(2022, 6, 6),
        },
        {
            "start": date(2022, 8, 29),
            "to": date(2022, 8, 30),
        },
        {
            "start": date(2022, 12, 26),
            "to": date(2022, 12, 28),
        },
        {
            "start": date(2022, 12, 27),
            "to": date(2022, 12, 28),
        },
        {
            "start": date(2023, 1, 2),
            "to": date(2023, 1, 3),
        },
        {
            "start": date(2023, 4, 7),
            "to": date(2023, 4, 11),
        },
        {
            "start": date(2023, 4, 10),
            "to": date(2023, 4, 11),
        },
        {
            "start": date(2023, 5, 1),
            "to": date(2023, 5, 2),
        },
        {
            "start": date(2023, 5, 29),
            "to": date(2023, 5, 30),
        },
        {
            "start": date(2023, 8, 28),
            "to": date(2023, 8, 29),
        },
        {
            "start": date(2023, 12, 26),
            "to": date(2023, 12, 28),
        },
        {
            "start": date(2023, 12, 27),
            "to": date(2023, 12, 28),
        },
    ]
    system_holidays = requests.get(
        "https://localhost:8443/fineract-provider/api/v1/holidays?officeId=1",
        verify=False,
        auth=HTTPBasicAuth("mifos", "password"),
        headers={"Fineract-Platform-TenantId": "default"},
    )
    assert system_holidays.status_code == 200
    for holiday in holidays:
        found = False
        for system in system_holidays.json():
            if holiday["start"] == date(*system["fromDate"]):
                found = True
                break
        if not found:
            r = requests.post(
                "https://localhost:8443/fineract-provider/api/v1/holidays/",
                verify=False,
                auth=HTTPBasicAuth("mifos", "password"),
                headers={"Fineract-Platform-TenantId": "default"},
                json={
                    "locale": "en",
                    "dateFormat": "dd MMMM yyyy",
                    "name": f"TEST - {holiday['start']}",
                    "fromDate": holiday["start"].strftime("%d %B %Y"),
                    "toDate": holiday["start"].strftime("%d %B %Y"),
                    "reschedulingType": 2,
                    "repaymentsRescheduledTo": holiday["to"].strftime("%d %B %Y"),
                    "offices": [{"officeId": 1}],
                },
            )
            assert r.status_code in [200, 403]
            if r.status_code == 200:
                r = requests.post(
                    f"https://localhost:8443/fineract-provider/api/v1/holidays/{r.json()['resourceId']}?command=Activate",
                    verify=False,
                    auth=HTTPBasicAuth("mifos", "password"),
                    headers={"Fineract-Platform-TenantId": "default"},
                    json={},
                )
                assert r.status_code in [
                    200,
                ]

    system_holidays = requests.get(
        "https://localhost:8443/fineract-provider/api/v1/holidays?officeId=1",
        verify=False,
        auth=HTTPBasicAuth("mifos", "password"),
        headers={"Fineract-Platform-TenantId": "default"},
    )
    assert system_holidays.status_code == 200
    assert len(system_holidays.json()) == len(holidays)


def find_in_account_list(name, list):
    for account in list:
        if account["name"] == name:
            return account["id"]


def account_configuration():
    accounts = requests.get(
        "https://localhost:8443/fineract-provider/api/v1/glaccounts",
        verify=False,
        auth=HTTPBasicAuth("mifos", "password"),
        headers={"Fineract-Platform-TenantId": "default"},
    )
    assert accounts.status_code == 200
    if len(accounts.json()) < len(fineract_configuration.accounts):
        for account in fineract_configuration.accounts:
            r = requests.post(
                "https://localhost:8443/fineract-provider/api/v1/glaccounts",
                verify=False,
                auth=HTTPBasicAuth("mifos", "password"),
                headers={"Fineract-Platform-TenantId": "default"},
                json={
                    "glCode": account["glCode"],
                    "manualEntriesAllowed": account["manualEntriesAllowed"],
                    "name": account["name"],
                    "type": account["type"]["id"],
                    "usage": account["usage"]["id"],
                },
            )
            if r.status_code not in [200, 403]:
                assert r.status_code == 200
        accounts = requests.get(
            "https://localhost:8443/fineract-provider/api/v1/glaccounts",
            verify=False,
            auth=HTTPBasicAuth("mifos", "password"),
            headers={"Fineract-Platform-TenantId": "default"},
        )
        assert accounts.status_code == 200
    account_mapping = {
        "fundSourceAccountId": find_in_account_list("Cash", accounts.json()),
        "loanPortfolioAccountId": find_in_account_list(
            "Loan Portfolio", accounts.json()
        ),
        "receivableInterestAccountId": find_in_account_list(
            "Receivables Interest", accounts.json()
        ),
        "receivableFeeAccountId": find_in_account_list(
            "Receivables Other", accounts.json()
        ),
        "receivablePenaltyAccountId": find_in_account_list(
            "Receivables Other", accounts.json()
        ),
        "transfersInSuspenseAccountId": find_in_account_list(
            "Suspense", accounts.json()
        ),
        "interestOnLoanAccountId": find_in_account_list(
            "Interest Income", accounts.json()
        ),
        "incomeFromFeeAccountId": find_in_account_list("Other Income", accounts.json()),
        "incomeFromPenaltyAccountId": find_in_account_list(
            "Other Income", accounts.json()
        ),
        "incomeFromRecoveryAccountId": find_in_account_list(
            "Other Income", accounts.json()
        ),
        "writeOffAccountId": find_in_account_list("Gross Writeoffs", accounts.json()),
        "overpaymentLiabilityAccountId": find_in_account_list(
            "Overpayment", accounts.json()
        ),
    }
    for key, value in account_mapping.items():
        fineract_configuration.quilam_loan[key] = value

    return fineract_configuration.quilam_loan


def loan_product_configuration(loanproduct):
    r = requests.get(
        "https://localhost:8443/fineract-provider/api/v1/funds",
        verify=False,
        auth=HTTPBasicAuth("mifos", "password"),
        headers={"Fineract-Platform-TenantId": "default"},
    )
    assert r.status_code == 200
    if len(r.json()) == 0:
        r = requests.post(
            "https://localhost:8443/fineract-provider/api/v1/funds",
            verify=False,
            auth=HTTPBasicAuth("mifos", "password"),
            headers={"Fineract-Platform-TenantId": "default"},
            json={"name": "Test fund"},
        )
        if r.status_code not in [200, 403]:
            assert r.status_code == 200

    r = requests.get(
        "https://localhost:8443/fineract-provider/api/v1/loanproducts",
        verify=False,
        auth=HTTPBasicAuth("mifos", "password"),
        headers={"Fineract-Platform-TenantId": "default"},
    )
    assert r.status_code == 200
    ql1 = None
    for product in r.json():
        if product["shortName"] == "ql1":
            ql1 = product
            break
    if not ql1:
        r = requests.post(
            "https://localhost:8443/fineract-provider/api/v1/loanproducts",
            verify=False,
            auth=HTTPBasicAuth("mifos", "password"),
            headers={"Fineract-Platform-TenantId": "default"},
            json=loanproduct,
        )
        if r.status_code not in [200, 403]:
            assert r.status_code == 200
    else:
        diff = False
        for key, value in loanproduct.items():
            if key in ql1 and ql1[key] != value:
                diff = True
                break
        if diff:
            r = requests.put(
                f"https://localhost:8443/fineract-provider/api/v1/loanproducts/{ql1['id']}",
                verify=False,
                auth=HTTPBasicAuth("mifos", "password"),
                headers={"Fineract-Platform-TenantId": "default"},
                json=loanproduct,
            )
            if r.status_code not in [200, 403]:
                assert r.status_code == 200


@pytest.fixture(scope="session", autouse=True)
def check_configuration():
    global_configuration()
    office_configuration()
    holiday_configuration()
    ql = account_configuration()
    loan_product_configuration(ql)
