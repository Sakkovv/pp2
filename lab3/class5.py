class Account:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Депозит в размере {amount} успешно выполнен. Новый баланс: {self.balance}")
        else:
            print("Неверная сумма для депозита. Депозит не выполнен.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Снятие средств в размере {amount} успешно выполнено. Новый баланс: {self.balance}")
        else:
            print("Неверная сумма для снятия." if amount <= 0 else "Недостаточно средств для снятия.")


owner_name = input("Введите имя владельца счета: ")
initial_balance = float(input("Введите начальный баланс: "))

account = Account(owner=owner_name, balance=initial_balance)

while True:
    action = input("Выберите действие (deposit/withdraw/exit): ").lower()

    if action == 'deposit':
        account.deposit(float(input("Введите сумму для депозита: ")))
    elif action == 'withdraw':
        account.withdraw(float(input("Введите сумму для снятия: ")))
    elif action == 'exit':
        break
    else:
        print("Неверное действие. Попробуйте снова.")
