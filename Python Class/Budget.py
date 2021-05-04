class Budget:
    def __init__(self, balance, name):
        self.balance = balance
        self.name = name

    def deposit_fund(self):
        amount = int(input('Please type in the amount you want to deposit: \n'))
        self.balance = self.balance + amount

    def withdraw_fund(self):
        amount_to_withdraw = int(input('Please type in the amount you want to withdraw: \n'))

        if amount_to_withdraw > self.get_balance() or amount_to_withdraw <= 0:
            print('You cannot withdraw that amount')
            self.withdraw_fund()
        else:
            self.balance = self.balance - amount_to_withdraw
            print('You withdrew ' + str(amount_to_withdraw) + ' successfully and your balance is ' + str(self.balance))
            return amount_to_withdraw

    def get_balance(self):
        return self.balance


def do_transaction(sender_object, recipient_object):
    amount_withdrawn = sender_object.withdraw_fund()
    recipient_object.balance = recipient_object.balance + amount_withdrawn
    print('You have successfully transferred ' + str(amount_withdrawn) + ' to ' + recipient_object.name + ' budget')


entertainment = Budget(4000000, 'Entertainment')
food = Budget(200000, 'Food')
cloth = Budget(300000, 'Cloth')
birthday = Budget(6000000, 'Birthday')
print('After creating instances')

do_transaction(entertainment, food)
