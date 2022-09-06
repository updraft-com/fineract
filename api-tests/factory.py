import uuid
from datetime import datetime

QL1 = None


def get_product(short_name, mifos_client):
    global QL1
    if short_name == "ql1" and QL1 is not None:
        return QL1
    r = mifos_client.request("get", "/loanproducts")
    assert r.status_code == 200
    for product in r.json():
        if product["shortName"] == short_name:
            if short_name == "ql1":
                QL1 = product
            return product
    assert False


def create_client(activationDate=datetime(2009, 1, 1, 12, 0, 0)):
    return {
        "officeId": 1,
        "legalFormId": 1,
        "firstname": str(uuid.uuid1()),
        "lastname": str(uuid.uuid1()),
        "externalId": str(uuid.uuid1()),
        # Mifos has a constraint that only one client can have one number
        # "mobileNo": user.profile.phone,
        "active": True,
        "activationDate": activationDate.strftime(format="%d %B %Y"),
        "dateFormat": "dd MMMM yyyy",
        "locale": "en",
        "address": [
            {
                "addressTypeId": 1,
                "isActive": True,
                "addressLine1": "",
                "addressLine2": "",
                "postalCode": "",
                "city": "",
            }
        ],
    }


def create_loan(
    clientId,
    product,
    submittedOnDate,
    princpal,
    duration,
    interestRate,
    repaymentsStartingFromDate=None,
):
    return {
        "dateFormat": "dd MMMM yyyy",
        "locale": "en_GB",
        "clientId": clientId,
        "productId": product["id"],
        "principal": princpal,
        "loanTermFrequency": duration,
        "loanTermFrequencyType": product["repaymentFrequencyType"]["id"],
        "loanType": "individual",
        "numberOfRepayments": duration,
        "repaymentEvery": product["repaymentEvery"],
        "repaymentFrequencyType": product["repaymentFrequencyType"]["id"],
        # Mifos expects a %
        "interestRatePerPeriod": interestRate,
        "amortizationType": product["amortizationType"]["id"],
        "interestType": product["interestType"]["id"],
        "interestCalculationPeriodType": product["interestCalculationPeriodType"]["id"],
        "transactionProcessingStrategyId": product["transactionProcessingStrategyId"],
        "expectedDisbursementDate": submittedOnDate.strftime(format="%d %B %Y"),
        "submittedOnDate": submittedOnDate.strftime(format="%d %B %Y"),
        "repaymentsStartingFromDate": repaymentsStartingFromDate.strftime(
            format="%d %B %Y"
        )
        if repaymentsStartingFromDate is not None
        else None,
    }


def create_loan_approval(approvedOnDate, amount, expectedDisbursementDate=None):
    return {
        "approvedOnDate": approvedOnDate.strftime(format="%d %B %Y"),
        "approvedLoanAmount": amount,
        "expectedDisbursementDate": expectedDisbursementDate.strftime(format="%d %B %Y")
        if expectedDisbursementDate
        else approvedOnDate.strftime(format="%d %B %Y"),
        "disbursementData": [],
        "locale": "en",
        "dateFormat": "dd MMMM yyyy",
    }


def create_loan_disbursal(
    actualDisbursementDate, amount, expectedDisbursementDate=None
):
    return {
        "paymentTypeId": 1,
        "transactionAmount": amount,
        "actualDisbursementDate": actualDisbursementDate.strftime(format="%d %B %Y"),
        "locale": "en",
        "dateFormat": "dd MMMM yyyy",
    }
