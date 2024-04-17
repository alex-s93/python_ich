# 2. Создайте класс BankAccount для представления банковского счета. Класс должен иметь атрибуты account_number
# (номер счета) и balance (баланс), а также методы deposit() для внесения денег на счет и withdraw() для снятия денег со
# счета. Затем создайте экземпляр класса BankAccount, внесите на счет некоторую сумму и снимите часть денег. Выведите
# оставшийся баланс. Не забудьте предусмотреть вариант, при котором при снятии баланс может стать меньше нуля. В этом
# случае уходить в минус не будем, вместо чего будем возвращать сообщение "Недостаточно средств на счете".

class BankAccount:
    def __init__(self, account_number: int, balance: float):
        self.account_number = account_number
        self.balance = balance

    # NOTE: принты добавлял для наглядности работы методов
    def deposit(self, amount: float):
        self.balance += amount
        print(f"You have successfully deposited {amount} to your bank account")

    def withdraw(self, amount: float):
        if self.balance < amount:
            print("Not enough money in the bank account. Check your balance and try again.")
        else:
            self.balance -= amount
            print(f"You have successfully withdrawn {amount} from your bank account")

    def show_balance(self):
        print("Your current balance:", self.balance)


if __name__ == "__main__":
    account = BankAccount(9023841234, 1000.00)

    account.show_balance()   # Your current balance: 1000.0
    account.deposit(100.5)   # You have successfully deposited 100.5 to your bank account
    account.withdraw(1200)   # Not enough money in the bank account. Check your balance and try again.
    account.withdraw(1000)   # You have successfully withdrawn 1000 from your bank account
    account.show_balance()   # Your current balance: 100.5
    account.withdraw(100.5)  # You have successfully withdrawn 100.5 from your bank account
    account.show_balance()   # Your current balance: 0.0
