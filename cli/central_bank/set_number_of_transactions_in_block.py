from cli.central_bank import SetFieldCommand


class SetNumberOfTransactionsInBlockCommand(SetFieldCommand):
    prefix_list = ('number', 'of', 'transaction', 'in', 'block')
    field_name = 'number_of_transactions_in_block'
    param_key = 'k'
