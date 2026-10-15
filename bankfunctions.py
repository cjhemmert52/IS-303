def withdraw(amount, balance):
    if amount > balance:
        raise Exception('Insufficient funds')

    return balance - amount