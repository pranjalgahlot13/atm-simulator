def check_balance(balance):
    print(f"Your current balance is: ${balance}")

def deposit(balance):
    amount = float(input("Enter deposit amount: "))
    balance += amount
    print(f"Successfully deposited ${amount}. New balance: ${balance}")
    return balance

def withdraw(balance):
    amount = float(input("Enter withdrawal amount: "))
    if amount > balance:
        print("Insufficient funds")
    else:
        balance -= amount
        print(f"Successfully withdrew ${amount}. New balance: ${balance}")
    return balance

balance = 1000

print("Welcome to the ATM!")

choice = 0
while choice != 4:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        balance = deposit(balance)
    elif choice == 2:
        balance = withdraw(balance)
    elif choice == 3:
        check_balance(balance)
    elif choice == 4:
        print("Goodbye")
    else:
        print("Invalid choice")