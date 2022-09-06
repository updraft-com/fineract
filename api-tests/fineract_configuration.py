import json

# from /fineract-provider/api/v1/glaccounts
accounts = json.loads(
    """
[
  {
    "id": 1,
    "name": "Interest Income",
    "glCode": "100",
    "disabled": false,
    "manualEntriesAllowed": true,
    "type": { "id": 4, "code": "accountType.income", "value": "INCOME" },
    "usage": { "id": 1, "code": "accountUsage.detail", "value": "DETAIL" },
    "nameDecorated": "Interest Income",
    "tagId": { "id": 0, "active": false, "mandatory": false }
  },
  {
    "id": 2,
    "name": "Other Income",
    "glCode": "101",
    "disabled": false,
    "manualEntriesAllowed": true,
    "type": { "id": 4, "code": "accountType.income", "value": "INCOME" },
    "usage": { "id": 1, "code": "accountUsage.detail", "value": "DETAIL" },
    "nameDecorated": "Other Income",
    "tagId": { "id": 0, "active": false, "mandatory": false }
  },
  {
    "id": 13,
    "name": "TEST",
    "glCode": "123",
    "disabled": false,
    "manualEntriesAllowed": true,
    "type": { "id": 1, "code": "accountType.asset", "value": "ASSET" },
    "usage": { "id": 1, "code": "accountUsage.detail", "value": "DETAIL" },
    "nameDecorated": "TEST",
    "tagId": { "id": 0, "active": false, "mandatory": false }
  },
  {
    "id": 3,
    "name": "Gross Writeoffs",
    "glCode": "200",
    "disabled": false,
    "manualEntriesAllowed": true,
    "type": { "id": 5, "code": "accountType.expense", "value": "EXPENSE" },
    "usage": { "id": 1, "code": "accountUsage.detail", "value": "DETAIL" },
    "nameDecorated": "Gross Writeoffs",
    "tagId": { "id": 0, "active": false, "mandatory": false }
  },
  {
    "id": 4,
    "name": "Provision Expense",
    "glCode": "201",
    "disabled": false,
    "manualEntriesAllowed": true,
    "type": { "id": 5, "code": "accountType.expense", "value": "EXPENSE" },
    "usage": { "id": 1, "code": "accountUsage.detail", "value": "DETAIL" },
    "nameDecorated": "Provision Expense",
    "tagId": { "id": 0, "active": false, "mandatory": false }
  },
  {
    "id": 5,
    "name": "Cash",
    "glCode": "300",
    "disabled": false,
    "manualEntriesAllowed": true,
    "type": { "id": 1, "code": "accountType.asset", "value": "ASSET" },
    "usage": { "id": 1, "code": "accountUsage.detail", "value": "DETAIL" },
    "nameDecorated": "Cash",
    "tagId": { "id": 0, "active": false, "mandatory": false }
  },
  {
    "id": 6,
    "name": "Loan Portfolio",
    "glCode": "400",
    "disabled": false,
    "manualEntriesAllowed": true,
    "type": { "id": 1, "code": "accountType.asset", "value": "ASSET" },
    "usage": { "id": 1, "code": "accountUsage.detail", "value": "DETAIL" },
    "nameDecorated": "Loan Portfolio",
    "tagId": { "id": 0, "active": false, "mandatory": false }
  },
  {
    "id": 7,
    "name": "Receivables Interest",
    "glCode": "500",
    "disabled": false,
    "manualEntriesAllowed": true,
    "type": { "id": 1, "code": "accountType.asset", "value": "ASSET" },
    "usage": { "id": 1, "code": "accountUsage.detail", "value": "DETAIL" },
    "nameDecorated": "Receivables Interest",
    "tagId": { "id": 0, "active": false, "mandatory": false }
  },
  {
    "id": 8,
    "name": "Receivables Other",
    "glCode": "501",
    "disabled": false,
    "manualEntriesAllowed": true,
    "type": { "id": 1, "code": "accountType.asset", "value": "ASSET" },
    "usage": { "id": 1, "code": "accountUsage.detail", "value": "DETAIL" },
    "nameDecorated": "Receivables Other",
    "tagId": { "id": 0, "active": false, "mandatory": false }
  },
  {
    "id": 9,
    "name": "Debt Fund",
    "glCode": "600",
    "disabled": false,
    "manualEntriesAllowed": true,
    "type": { "id": 2, "code": "accountType.liability", "value": "LIABILITY" },
    "usage": { "id": 1, "code": "accountUsage.detail", "value": "DETAIL" },
    "nameDecorated": "Debt Fund",
    "tagId": { "id": 0, "active": false, "mandatory": false }
  },
  {
    "id": 10,
    "name": "Overpayment",
    "glCode": "610",
    "disabled": false,
    "manualEntriesAllowed": true,
    "type": { "id": 2, "code": "accountType.liability", "value": "LIABILITY" },
    "usage": { "id": 1, "code": "accountUsage.detail", "value": "DETAIL" },
    "nameDecorated": "Overpayment",
    "tagId": { "id": 0, "active": false, "mandatory": false }
  },
  {
    "id": 11,
    "name": "Provision Pool",
    "glCode": "700",
    "disabled": false,
    "manualEntriesAllowed": true,
    "type": { "id": 1, "code": "accountType.asset", "value": "ASSET" },
    "usage": { "id": 1, "code": "accountUsage.detail", "value": "DETAIL" },
    "nameDecorated": "Provision Pool",
    "tagId": { "id": 0, "active": false, "mandatory": false }
  },
  {
    "id": 12,
    "name": "Suspense",
    "glCode": "800",
    "disabled": false,
    "manualEntriesAllowed": true,
    "type": { "id": 1, "code": "accountType.asset", "value": "ASSET" },
    "usage": { "id": 1, "code": "accountUsage.detail", "value": "DETAIL" },
    "nameDecorated": "Suspense",
    "tagId": { "id": 0, "active": false, "mandatory": false }
  }
]
"""
)

# from /fineract-provider/api/v1/loanproducts
quilam_loan = json.loads(
    """
{
  "name": "Quilam Loan",
  "shortName": "ql1",
  "fundId": 1,
  "includeInBorrowerCycle": false,
  "useBorrowerCycle": false,
  "currencyCode": "GBP",
  "digitsAfterDecimal": 2,
  "inMultiplesOf": 0,
  "principal": 3000,
  "minPrincipal": 100,
  "maxPrincipal": "21000",
  "numberOfRepayments": 36,
  "minNumberOfRepayments": 3,
  "maxNumberOfRepayments": 60,
  "repaymentEvery": 1,
  "repaymentFrequencyType": 2,
  "interestRatePerPeriod": 19.9,
  "minInterestRatePerPeriod": 5.9,
  "maxInterestRatePerPeriod": 35.9,
  "interestRateFrequencyType": 3,
  "amortizationType": 1,
  "fixedPrincipalPercentagePerInstallment": null,
  "interestType": 0,
  "interestCalculationPeriodType": 0,
  "allowPartialPeriodInterestCalcualtion": false,
  "transactionProcessingStrategyId": 6,
  "graceOnArrearsAgeing": 7,
  "overdueDaysForNPA": 90,
  "accountMovesOutOfNPAOnlyOnArrearsCompletion": false,
  "accountingRule": 3,
  "principalVariationsForBorrowerCycle": [],
  "interestRateVariationsForBorrowerCycle": [],
  "numberOfRepaymentVariationsForBorrowerCycle": [],
  "multiDisburseLoan": false,
  "maxTrancheCount": 0,
  "daysInYearType": 1,
  "daysInMonthType": 1,
  "isInterestRecalculationEnabled": true,
  "holdGuaranteeFunds": false,
  "minimumDaysBetweenDisbursalAndFirstRepayment": 7,
  "principalThresholdForLastInstallment": 0,
  "canDefineInstallmentAmount": true,
  "isEqualAmortization": false,
  "interestRecalculationCompoundingMethod": 0,
  "rescheduleStrategyMethod": 2,
  "recalculationRestFrequencyType": 2,
  "recalculationRestFrequencyInterval": 0,
  "isArrearsBasedOnOriginalSchedule": false,
  "preClosureInterestCalculationStrategy": 1,
  "fundSourceAccountId": 5,
  "loanPortfolioAccountId": 6,
  "receivableInterestAccountId": 7,
  "receivableFeeAccountId": 8,
  "receivablePenaltyAccountId": 8,
  "transfersInSuspenseAccountId": 12,
  "interestOnLoanAccountId": 1,
  "incomeFromFeeAccountId": 2,
  "incomeFromPenaltyAccountId": 2,
  "incomeFromRecoveryAccountId": 2,
  "writeOffAccountId": 3,
  "overpaymentLiabilityAccountId": 10,
  "isLinkedToFloatingInterestRates": false,
  "allowVariableInstallments": false,
  "canUseForTopup": true,
  "rates": [],
  "paymentChannelToFundSourceMappings": [],
  "feeToIncomeAccountMappings": [],
  "penaltyToIncomeAccountMappings": [],
  "charges": [],
  "allowAttributeOverrides": {
    "amortizationType": true,
    "interestType": true,
    "transactionProcessingStrategyId": true,
    "interestCalculationPeriodType": true,
    "inArrearsTolerance": true,
    "repaymentEvery": true,
    "graceOnPrincipalAndInterestPayment": true,
    "graceOnArrearsAgeing": true
  },
  "dateFormat": "dd MMMM yyyy",
  "locale": "en"
}
"""
)

# from /fineract-provider/api/v1/configurations
configurations = json.loads(
    """
{
  "globalConfiguration": [
    {
      "name": "maker-checker",
      "enabled": false,
      "value": 0,
      "id": 1,
      "trapDoor": false
    },
    {
      "name": "amazon-S3",
      "enabled": true,
      "value": 1,
      "id": 4,
      "trapDoor": false
    },
    {
      "name": "reschedule-future-repayments",
      "enabled": true,
      "value": 1,
      "id": 5,
      "trapDoor": false
    },
    {
      "name": "reschedule-repayments-on-holidays",
      "enabled": false,
      "value": 0,
      "id": 6,
      "trapDoor": false
    },
    {
      "name": "allow-transactions-on-holiday",
      "enabled": true,
      "value": 1,
      "id": 7,
      "trapDoor": false
    },
    {
      "name": "allow-transactions-on-non_workingday",
      "enabled": true,
      "value": 1,
      "id": 8,
      "trapDoor": false
    },
    {
      "name": "constraint_approach_for_datatables",
      "enabled": false,
      "value": 0,
      "id": 9,
      "trapDoor": false
    },
    {
      "name": "penalty-wait-period",
      "enabled": true,
      "value": 2,
      "id": 10,
      "trapDoor": false
    },
    {
      "name": "force-password-reset-days",
      "enabled": false,
      "value": 0,
      "id": 11,
      "trapDoor": false
    },
    {
      "name": "grace-on-penalty-posting",
      "enabled": true,
      "value": 0,
      "id": 12,
      "trapDoor": false
    },
    {
      "name": "savings-interest-posting-current-period-end",
      "enabled": false,
      "value": 0,
      "id": 15,
      "description": "Recommended to be changed only once during start of production. When set as false(default), interest will be posted on the first date of next period. If set as true, interest will be posted on last date of current period. There is no difference in the interest amount posted.",
      "trapDoor": false
    },
    {
      "name": "financial-year-beginning-month",
      "enabled": true,
      "value": 1,
      "id": 16,
      "description": "Recommended to be changed only once during start of production. Allowed values 1 - 12 (January - December). Interest posting periods are evaluated based on this configuration.",
      "trapDoor": false
    },
    {
      "name": "min-clients-in-group",
      "enabled": false,
      "value": 5,
      "id": 17,
      "description": "Minimum number of Clients that a Group should have",
      "trapDoor": false
    },
    {
      "name": "max-clients-in-group",
      "enabled": false,
      "value": 5,
      "id": 18,
      "description": "Maximum number of Clients that a Group can have",
      "trapDoor": false
    },
    {
      "name": "meetings-mandatory-for-jlg-loans",
      "enabled": false,
      "value": 0,
      "id": 19,
      "description": "Enforces all JLG loans to follow a meeting schedule belonging to parent group or Center",
      "trapDoor": false
    },
    {
      "name": "office-specific-products-enabled",
      "enabled": false,
      "value": 0,
      "id": 20,
      "description": "Whether products and fees should be office specific or not? This property should NOT be changed once Mifos is Live.",
      "trapDoor": false
    },
    {
      "name": "restrict-products-to-user-office",
      "enabled": false,
      "value": 0,
      "id": 21,
      "description": "This should be enabled only if, products \u0026 fees are office specific (i.e. office-specific-products-enabled is enabled). This property specifies if the products should be auto-restricted to office of the user who created the proudct? Note: This property should NOT be changed once Mifos is Live.",
      "trapDoor": false
    },
    {
      "name": "office-opening-balances-contra-account",
      "enabled": true,
      "value": 0,
      "id": 22,
      "trapDoor": false
    },
    {
      "name": "rounding-mode",
      "enabled": true,
      "value": 6,
      "id": 23,
      "description": "0 - UP, 1 - DOWN, 2- CEILING, 3- FLOOR, 4- HALF_UP, 5- HALF_DOWN, 6 - HALF_EVEN",
      "trapDoor": true
    },
    {
      "name": "backdate-penalties-enabled",
      "enabled": true,
      "value": 0,
      "id": 24,
      "description": "If this parameter is disabled penalties will only be added to instalments due moving forward, any old overdue instalments will not be affected.",
      "trapDoor": false
    },
    {
      "name": "organisation-start-date",
      "enabled": false,
      "value": 0,
      "id": 25,
      "trapDoor": false
    },
    {
      "name": "paymenttype-applicable-for-disbursement-charges",
      "enabled": false,
      "value": 0,
      "id": 26,
      "description": "Is the Disbursement Entry need to be considering the fund source of the paymnet type",
      "trapDoor": false
    },
    {
      "name": "interest-charged-from-date-same-as-disbursal-date",
      "enabled": true,
      "value": 0,
      "id": 27,
      "trapDoor": false
    },
    {
      "name": "skip-repayment-on-first-day-of-month",
      "enabled": false,
      "value": 14,
      "id": 28,
      "description": "skipping repayment on first day of month",
      "trapDoor": false
    },
    {
      "name": "change-emi-if-repaymentdate-same-as-disbursementdate",
      "enabled": true,
      "value": 0,
      "id": 29,
      "description": "In tranche loans, if repayment date is same as tranche disbursement date then allow to change the emi amount",
      "trapDoor": false
    },
    {
      "name": "daily-tpt-limit",
      "enabled": false,
      "value": 0,
      "id": 30,
      "description": "Daily limit for third party transfers",
      "trapDoor": false
    },
    {
      "name": "Enable-Address",
      "enabled": true,
      "value": 0,
      "id": 31,
      "trapDoor": false
    },
    {
      "name": "sub-rates",
      "enabled": false,
      "value": 0,
      "id": 32,
      "description": "Enable Rates Module",
      "trapDoor": false
    },
    {
      "name": "loan-reschedule-is-first-payday-allowed-on-holiday",
      "enabled": false,
      "value": 0,
      "id": 33,
      "description": "If enabled, while loan reschedule the first repayment date can be on a holiday/non working day",
      "trapDoor": false
    },
    {
      "name": "account-mapping-for-payment-type",
      "enabled": true,
      "value": 0,
      "stringValue": "Asset",
      "id": 35,
      "description": "Asset: default for asset, Use comma seperated values for Liability, Asset and Expense accounts",
      "trapDoor": false
    },
    {
      "name": "account-mapping-for-charge",
      "enabled": true,
      "value": 0,
      "stringValue": "Income",
      "id": 36,
      "description": "Income: default for Income, Use comma seperated values for Income, Liability and Expense accounts",
      "trapDoor": false
    },
    {
      "name": "fixed-deposit-transfer-interest-next-day-for-period-end-posting",
      "enabled": false,
      "value": 0,
      "id": 37,
      "description": "Transfer fixed transfer interest next day(t+1) for period end posting",
      "trapDoor": false
    },
    {
      "name": "allow-backdated-transaction-before-interest-posting",
      "enabled": true,
      "value": 0,
      "id": 38,
      "description": "Avoid retrieving all transactions in a savings account",
      "trapDoor": false
    },
    {
      "name": "allow-backdated-transaction-before-interest-posting-date-for-days",
      "enabled": false,
      "value": 0,
      "id": 39,
      "description": "One time configuration to relax the backdated transactions",
      "trapDoor": false
    },
    {
      "name": "custom-account-number-length",
      "enabled": false,
      "value": 0,
      "id": 40,
      "description": "if enabled, the value if this configuration will set accounnumber length",
      "trapDoor": false
    },
    {
      "name": "random-account-number",
      "enabled": false,
      "value": 0,
      "id": 41,
      "description": "if enabled, the client accounts, saving accounts, loan accounts will be created with Random Account Number",
      "trapDoor": false
    },
    {
      "name": "is-interest-to-be-recovered-first-when-greater-than-emi",
      "enabled": true,
      "value": 0,
      "id": 42,
      "description": "If enabled, when interest amount is greater than EMI, the additional interest is recovered first before principal",
      "trapDoor": false
    },
    {
      "name": "is-principal-compounding-disabled-for-overdue-loans",
      "enabled": false,
      "value": 0,
      "id": 43,
      "description": "If enabled, it donot consider principal of an unpaid installment for calculating interest of next installment. this is for testing back-dated loan schedule",
      "trapDoor": false
    }
  ]
}
"""
)
