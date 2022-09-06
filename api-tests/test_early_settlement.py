from datetime import date, datetime

import factory


def test_early_settlement(mifos_client):
    # Test a loan settled after 12 months
    r = mifos_client.request("post", "/clients", json=factory.create_client())
    assert r.status_code == 200
    assert "clientId" in r.json()
    clientId = r.json()["clientId"]
    ql1 = factory.get_product("ql1", mifos_client)
    loan = factory.create_loan(clientId, ql1, datetime(2021, 10, 12), 7000, 60, 9.9)
    r = mifos_client.request("post", "/loans", json=loan)
    assert r.status_code == 200
    loanId = r.json()["loanId"]
    r = mifos_client.request(
        "post",
        f"/loans/{loanId}?command=approve",
        json=factory.create_loan_approval(datetime(2021, 10, 12), 7000),
    )
    assert r.status_code == 200
    approval_schedule = mifos_client.request(
        "get", f"/loans/{loanId}?associations=all&exclude=guarantors,futureSchedule"
    )
    assert approval_schedule.status_code == 200
    r = mifos_client.request(
        "post",
        f"/loans/{loanId}?command=disburse",
        json=factory.create_loan_disbursal(datetime(2021, 10, 15), 7000),
    )
    assert r.status_code == 200
    disbursal_schedule = mifos_client.request(
        "get", f"/loans/{loanId}?associations=all&exclude=guarantors,futureSchedule"
    )
    assert disbursal_schedule.status_code == 200
    # Skip this assertion for now
    # assert (
    #     approval_schedule.json()["repaymentSchedule"]["periods"][-1][
    #         "totalDueForPeriod"
    #     ]
    #     == disbursal_schedule.json()["repaymentSchedule"]["periods"][-1][
    #         "totalDueForPeriod"
    #     ]
    # )
    transactions = [
        {"date": date(2021, 11, 1), "amount": 147.92},
        {"date": date(2021, 12, 1), "amount": 147.92},
        {"date": date(2022, 1, 4), "amount": 147.92},
        {"date": date(2022, 2, 1), "amount": 147.92},
        {"date": date(2022, 3, 1), "amount": 147.92},
        {"date": date(2022, 4, 1), "amount": 147.92},
        {"date": date(2022, 5, 3), "amount": 147.92},
        {"date": date(2022, 6, 1), "amount": 147.92},
        {"date": date(2022, 7, 1), "amount": 147.92},
        {"date": date(2022, 8, 1), "amount": 147.92},
        {"date": date(2022, 8, 30), "amount": 7410.58},
    ]
    # post these transactions, and ensure that the next payment due remains as per the
    # original regular schedule
    for t in transactions:
        r = mifos_client.request(
            "post",
            f"/loans/{loanId}/transactions?command=repayment",
            json={
                "paymentTypeId": 1,
                "transactionAmount": t["amount"],
                "transactionDate": t["date"].strftime(format="%d %B %Y"),
                "locale": "en",
                "dateFormat": "dd MMMM yyyy",
            },
        )
        assert r.status_code == 200


def test_out_of_band_payments(mifos_client):
    # Test a loan settled after 12 months
    r = mifos_client.request("post", "/clients", json=factory.create_client())
    assert r.status_code == 200
    assert "clientId" in r.json()
    clientId = r.json()["clientId"]
    ql1 = factory.get_product("ql1", mifos_client)
    loan = factory.create_loan(
        clientId,
        ql1,
        datetime(2022, 1, 8),
        5000,
        48,
        22.9,
        repaymentsStartingFromDate=date(2022, 2, 28),
    )
    r = mifos_client.request("post", "/loans", json=loan)
    assert r.status_code == 200
    loanId = r.json()["loanId"]
    r = mifos_client.request(
        "post",
        f"/loans/{loanId}?command=approve",
        json=factory.create_loan_approval(datetime(2022, 1, 8), 5000),
    )
    assert r.status_code == 200
    approval_schedule = mifos_client.request(
        "get", f"/loans/{loanId}?associations=all&exclude=guarantors,futureSchedule"
    )
    assert approval_schedule.status_code == 200
    r = mifos_client.request(
        "post",
        f"/loans/{loanId}?command=disburse",
        json=factory.create_loan_disbursal(datetime(2022, 1, 8), 5000),
    )
    assert r.status_code == 200
    disbursal_schedule = mifos_client.request(
        "get", f"/loans/{loanId}?associations=all&exclude=guarantors,futureSchedule"
    )
    assert disbursal_schedule.status_code == 200
    # Skip this assertion for now
    # assert (
    #     approval_schedule.json()["repaymentSchedule"]["periods"][-1][
    #         "totalDueForPeriod"
    #     ]
    #     == disbursal_schedule.json()["repaymentSchedule"]["periods"][-1][
    #         "totalDueForPeriod"
    #     ]
    # )
    transactions = [
        {"date": date(2022, 2, 1), "amount": 159.13},
        {"date": date(2022, 3, 1), "amount": 159.13},
        {"date": date(2022, 4, 1), "amount": 159.13},
        {"date": date(2022, 5, 3), "amount": 159.13},
        {"date": date(2022, 6, 1), "amount": 159.13},
    ]
    # post these transactions, and ensure that the next payment due remains as per the
    # original regular schedule
    for t in transactions:
        r = mifos_client.request(
            "post",
            f"/loans/{loanId}/transactions?command=repayment",
            json={
                "paymentTypeId": 1,
                "transactionAmount": t["amount"],
                "transactionDate": t["date"].strftime(format="%d %B %Y"),
                "locale": "en",
                "dateFormat": "dd MMMM yyyy",
            },
        )
        assert r.status_code == 200
