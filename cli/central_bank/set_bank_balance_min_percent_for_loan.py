from cli.central_bank import SetFieldCommand


class SetBankBalanceMinPercentForLoanCommand(SetFieldCommand):
    prefix_list = ('bank', 'balance')
    postfix_list = ('more', 'than', 'the', 'requesting', 'loan')

    field_name = 'bank_balance_min_percent_for_loan'
    param_key = '%s'
