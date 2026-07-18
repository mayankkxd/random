def show_balance():
    print(f"Your balance is {balance}")
def deposit():
    depo = float(input("Enter amount to be deposited: "))
    return depo
def withdraw():
    withd = float(input("Enter amount to be withdrawn: "))
    return withd
print("Welcome to the Bank!")
balance = float(input("Enter your balance: "))
purse = float(input("Enter your wallet amount: "))
print("1. Show Balance")
print("2. Deposit")
print("3. Withdraw")
choice = input("Enter your choice (1/2/3): ")
match choice:
    case "1":
        show_balance()
    case "2":
        depo = deposit()
        if depo <= purse:
            print(f"Your new balance is {balance + depo}")
            print(f"Your wallet now has {purse - depo}")
        else:
            print("Your deposit amount exceeds your wallet amount. Transaction failed.")
    case "3":
        withd = withdraw()
        if withd <= balance:
            print(f"Your new balance is {balance - withd}")
            print(f"Your wallet now has {purse + withd}")
        else:
            print("Your withdraw amount exceeds your balance. Transaction failed")
    case _:
        print("Invalid choice")
            

                    

