#constructor, destructor
#creating bank account and list out the customer details

class Bank_account:
    def __init__(self, customer_name, balance, account_no):
        self.customer_name = customer_name
        self.balance = balance
        self.account_no = account_no

    def __str__(self):
        return self.customer_name

#create a object for this class and change member variable
#object
customer1 = Bank_account("Rocky",10000000001,1447056398)
customer2 = Bank_account("berlin",250460000,635924632)
'''customer1.customer_name = "maker"
customer1.balance = 100000000
customer1.account_no = 12345'''

print(customer1.customer_name,customer1.balance,customer1.account_no)
print(customer2.customer_name,customer2.account_no,customer2.balance)
print(customer1,customer2)