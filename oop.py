
class Budget:
    def __init__(self, balance, deposit, withdrawal, category):
        self.balance = balance
        self.deposit = deposit
        self.withdrawal = withdrawal
        self.category = category

    def budget_calc(self):
        self.balance = self.balance + self.deposit - self.withdrawal
        return f'This is the {self.category} balance: {self.balance}, {self.category} deposit: {self.deposit} and {self.category} withdrawal: {self.withdrawal}.'



#Balance for all the three categories
food_balance = Budget(5000, 0, 0, 'food')
clothing_balance = Budget(20000, 0, 0, 'clothing')
entertainment_balance = Budget(10000, 0, 0, 'entertainment')


#Deposit for the three categories
food_deposit = Budget(5000, 7000, 0, 'food')
clothing_deposit = Budget(20000, 45000, 0, 'clothing')
entertainment_deposit = Budget(10000, 25000, 0, 'entertainment')


#Withdrawal for the three categories
food_withdrawal = Budget(12000, 0, 10500, 'food')
clothing_withdrawal = Budget(65000, 0, 50000, 'clothing')
entertainment_withdrawal = Budget(35000, 0, 28500, 'entertainment')

print(food_balance.budget_calc())
print(clothing_balance.budget_calc())
print(entertainment_balance.budget_calc())
print('*' * 80)
print('*' * 80)
print(food_deposit.budget_calc())
print(clothing_deposit.budget_calc())
print(entertainment_deposit.budget_calc())
print('*' * 80)
print('*' * 80)
print(food_withdrawal.budget_calc())
print(clothing_withdrawal.budget_calc())
print(entertainment_withdrawal.budget_calc())

#Balances of food after withdrawal
print(f'Food balance:{food_withdrawal.balance}')

#Balances of clothing after withdrawal
print(f'Clothing balance:{clothing_withdrawal.balance}')

#Balances of entertainment after withdrawal
print(f'entertainment balance: {entertainment_withdrawal.balance}')


#Transfer of food balance to clothing Balance
print(f'Transfer of food balance to clothing Balance: {food_withdrawal.balance + clothing_withdrawal.balance}')

#Transfer of clothing balance to entertainment balance
print(f'Transfer of clothing balance to entertainment balance: {clothing_withdrawal.balance + entertainment_withdrawal.balance}')
#Transfer of entertainment balance to food balance
print(f'Transfer of entertainment balance to food balance: {entertainment_withdrawal.balance + food_withdrawal.balance}')

#Total balance of the food, entertainment and clothing Balances

print(f'Total balance of the food, entertainment and clothing Balances: {food_withdrawal.balance + clothing_withdrawal.balance + entertainment_withdrawal.balance}')
