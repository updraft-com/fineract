from datetime import date, datetime

import pytz

from conftest import find_in_reference_configuration
import factory
from datetime import datetime


def test_create_loan_make_repayments_per_approved_schedule(mifos_client):
    r = mifos_client.request("post", "/clients", json=factory.create_client())
    assert r.status_code == 200
    assert "clientId" in r.json()
    clientId = r.json()["clientId"]
    ql1 = factory.get_product("ql1", mifos_client)
    loan = factory.create_loan(
        clientId, ql1, datetime(2015, 1, 1, 12, 0, 0), 3000, 36, 19.9
    )
    r = mifos_client.request("post", "/loans", json=loan)
    assert r.status_code == 200
    loanId = r.json()["loanId"]
    r = mifos_client.request(
        "post",
        f"/loans/{loanId}?command=approve",
        json=factory.create_loan_approval(datetime(2015, 1, 1, 12, 0, 0), 3000),
    )
    assert r.status_code == 200
    schedule = mifos_client.request(
        "get", f"/loans/{loanId}?associations=all&exclude=guarantors,futureSchedule"
    )
    assert schedule.status_code == 200
    r = mifos_client.request(
        "post",
        f"/loans/{loanId}?command=disburse",
        json=factory.create_loan_disbursal(datetime(2015, 1, 1, 12, 0, 0), 3000),
    )
    assert r.status_code == 200
    # Now let's test we can post transactions against the loan
    # Let's post the scheduled payments
    for period in schedule.json()["repaymentSchedule"]["periods"]:
        if period["totalDueForPeriod"] > 0:
            d = date(*period["dueDate"])
            r = mifos_client.request(
                "post",
                f"/loans/{loanId}/transactions?command=repayment",
                json={
                    "paymentTypeId": 1,
                    "transactionAmount": period["totalDueForPeriod"],
                    "transactionDate": d.strftime(format="%d %B %Y"),
                    "locale": "en",
                    "dateFormat": "dd MMMM yyyy",
                },
            )
            assert r.status_code == 200
    r = mifos_client.request(
        "get", f"/loans/{loanId}?associations=all&exclude=guarantors,futureSchedule"
    )
    assert r.status_code == 200
    assert r.json()["status"]["code"] == "loanStatusType.closed.obligations.met"


def test_create_loan_make_repayments_per_disbursed_schedule(mifos_client):
    r = mifos_client.request("post", "/clients", json=factory.create_client())
    assert r.status_code == 200
    assert "clientId" in r.json()
    clientId = r.json()["clientId"]
    ql1 = factory.get_product("ql1", mifos_client)
    loan = factory.create_loan(
        clientId, ql1, datetime(2015, 1, 1, 12, 0, 0), 3000, 36, 19.9
    )
    r = mifos_client.request("post", "/loans", json=loan)
    assert r.status_code == 200
    loanId = r.json()["loanId"]
    r = mifos_client.request(
        "post",
        f"/loans/{loanId}?command=approve",
        json=factory.create_loan_approval(datetime(2015, 1, 1, 12, 0, 0), 3000),
    )
    assert r.status_code == 200
    r = mifos_client.request(
        "post",
        f"/loans/{loanId}?command=disburse",
        json=factory.create_loan_disbursal(datetime(2015, 1, 1, 12, 0, 0), 3000),
    )
    assert r.status_code == 200
    # Now let's test we can post transactions against the loan
    # Let's post the scheduled payments
    schedule = mifos_client.request(
        "get", f"/loans/{loanId}?associations=all&exclude=guarantors,futureSchedule"
    )
    assert schedule.status_code == 200
    for period in schedule.json()["repaymentSchedule"]["periods"]:
        if period["totalDueForPeriod"] > 0:
            d = date(*period["dueDate"])
            r = mifos_client.request(
                "post",
                f"/loans/{loanId}/transactions?command=repayment",
                json={
                    "paymentTypeId": 1,
                    "transactionAmount": period["totalDueForPeriod"],
                    "transactionDate": d.strftime(format="%d %B %Y"),
                    "locale": "en",
                    "dateFormat": "dd MMMM yyyy",
                },
            )
            assert r.status_code == 200
    r = mifos_client.request(
        "get", f"/loans/{loanId}?associations=all&exclude=guarantors,futureSchedule"
    )
    assert r.status_code == 200
    assert r.json()["status"]["code"] == "loanStatusType.closed.obligations.met"


def test_create_loan_make_repayments_next_payment(mifos_client):
    r = mifos_client.request("post", "/clients", json=factory.create_client())
    assert r.status_code == 200
    assert "clientId" in r.json()
    clientId = r.json()["clientId"]
    ql1 = factory.get_product("ql1", mifos_client)
    loan = factory.create_loan(
        clientId, ql1, datetime(2018, 1, 1, 12, 0, 0), 3000, 36, 19.9
    )
    r = mifos_client.request("post", "/loans", json=loan)
    assert r.status_code == 200
    loanId = r.json()["loanId"]
    r = mifos_client.request(
        "post",
        f"/loans/{loanId}?command=approve",
        json=factory.create_loan_approval(datetime(2018, 1, 1, 12, 0, 0), 3000),
    )
    assert r.status_code == 200
    r = mifos_client.request(
        "post",
        f"/loans/{loanId}?command=disburse",
        json=factory.create_loan_disbursal(datetime(2018, 1, 1, 12, 0, 0), 3000),
    )
    assert r.status_code == 200
    # Now let's test we can post transactions against the loan
    # Let's post the scheduled payments
    complete = False
    while not complete:
        schedule = mifos_client.request(
            "get", f"/loans/{loanId}?associations=all&exclude=guarantors,futureSchedule"
        )
        assert schedule.status_code == 200
        complete = True
        for period in schedule.json()["repaymentSchedule"]["periods"]:
            if not period.get("complete", True):
                # make a payment to complete this period
                complete = False
                d = date(*period["dueDate"])
                r = mifos_client.request(
                    "post",
                    f"/loans/{loanId}/transactions?command=repayment",
                    json={
                        "paymentTypeId": 1,
                        "transactionAmount": period["totalOutstandingForPeriod"],
                        "transactionDate": d.strftime(format="%d %B %Y"),
                        "locale": "en",
                        "dateFormat": "dd MMMM yyyy",
                    },
                )
                assert r.status_code == 200
    r = mifos_client.request(
        "get", f"/loans/{loanId}?associations=all&exclude=guarantors,futureSchedule"
    )
    assert r.status_code == 200
    assert r.json()["status"]["code"] == "loanStatusType.closed.obligations.met"


def test_create_loan_final_payment_in_future(mifos_client):
    # If the final payment is in the future does disbursing change from original?
    r = mifos_client.request("post", "/clients", json=factory.create_client())
    assert r.status_code == 200
    assert "clientId" in r.json()
    clientId = r.json()["clientId"]
    ql1 = factory.get_product("ql1", mifos_client)
    loan = factory.create_loan(
        clientId, ql1, datetime(2021, 1, 1, 12, 0, 0), 3000, 36, 19.9
    )
    r = mifos_client.request("post", "/loans", json=loan)
    assert r.status_code == 200
    loanId = r.json()["loanId"]
    r = mifos_client.request(
        "post",
        f"/loans/{loanId}?command=approve",
        json=factory.create_loan_approval(datetime(2021, 1, 1, 12, 0, 0), 3000),
    )
    assert r.status_code == 200
    approval_schedule = mifos_client.request(
        "get", f"/loans/{loanId}?associations=all&exclude=guarantors,futureSchedule"
    )
    assert approval_schedule.status_code == 200
    r = mifos_client.request(
        "post",
        f"/loans/{loanId}?command=disburse",
        json=factory.create_loan_disbursal(datetime(2021, 1, 1, 12, 0, 0), 3000),
    )
    assert r.status_code == 200
    disbursal_schedule = mifos_client.request(
        "get", f"/loans/{loanId}?associations=all&exclude=guarantors,futureSchedule"
    )
    assert disbursal_schedule.status_code == 200
    assert (
        approval_schedule.json()["repaymentSchedule"]["periods"][-1][
            "totalDueForPeriod"
        ]
        == disbursal_schedule.json()["repaymentSchedule"]["periods"][-1][
            "totalDueForPeriod"
        ]
    )


def test_create_loan_all_loan_in_future(mifos_client):
    # If the final payment is in the future does disbursing change from original?
    r = mifos_client.request("post", "/clients", json=factory.create_client())
    assert r.status_code == 200
    assert "clientId" in r.json()
    clientId = r.json()["clientId"]
    ql1 = factory.get_product("ql1", mifos_client)
    loan = factory.create_loan(
        clientId, ql1, datetime.utcnow().replace(tzinfo=pytz.utc), 3000, 36, 19.9
    )
    r = mifos_client.request("post", "/loans", json=loan)
    assert r.status_code == 200
    loanId = r.json()["loanId"]
    r = mifos_client.request(
        "post",
        f"/loans/{loanId}?command=approve",
        json=factory.create_loan_approval(datetime.utcnow().replace(tzinfo=pytz.utc), 3000),
    )
    assert r.status_code == 200
    approval_schedule = mifos_client.request(
        "get", f"/loans/{loanId}?associations=all&exclude=guarantors,futureSchedule"
    )
    assert approval_schedule.status_code == 200
    r = mifos_client.request(
        "post",
        f"/loans/{loanId}?command=disburse",
        json=factory.create_loan_disbursal(datetime.utcnow().replace(tzinfo=pytz.utc), 3000),
    )
    assert r.status_code == 200
    disbursal_schedule = mifos_client.request(
        "get", f"/loans/{loanId}?associations=all&exclude=guarantors,futureSchedule"
    )
    assert disbursal_schedule.status_code == 200
    assert (
        approval_schedule.json()["repaymentSchedule"]["periods"][-1][
            "totalDueForPeriod"
        ]
        == disbursal_schedule.json()["repaymentSchedule"]["periods"][-1][
            "totalDueForPeriod"
        ]
    )
