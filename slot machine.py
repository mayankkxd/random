import random
import time
def spin():
    row = ['🍎', '🍌', '⭐']
    return [random.choice(row) for symbol in range(3)]
def printrow(row):
    print()
    print("-----------------------------------------")
    print()
    print("\t\t".join(row))
    print()
    print("-----------------------------------------")
    print()
def payout(row):
    if row[0] == row[1] == row[2]:
        return 1
    else:
        return 0
def main():
    print("****************************")
    print("Welcome to slots machine!")
    print("Symbols are: 🍎  🍌  ⭐")
    print("****************************")
    balance = int(input("Enter your balance: "))
    while balance > 0:
        bet = input("Enter the amount to bet: (press q to quit): ")
        if bet == 'q':
            print("You quit.")
            break
        else:
            if not bet.isdigit():
                print("Invalid bet amount.")
                continue

            bet = int(bet)

            if balance < bet:
                print("Insufficient funds.")
                continue

            if bet <= 0:
                print("Invalid bet amount.")
                continue

            print("Spinning...")
            time.sleep(1)
            print("..")
            time.sleep(1)
            print("..")
            time.sleep(1)
            row = spin()
            printrow(row)
            balance -= bet
            if payout(row) == 1:
                print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
                print("YOU WIN!!")
                print("You doubled your bet.")
                print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
                balance += bet*2
                print(f"Your new balance is ${balance:.2f}")
                print("-----------------------------------------")
            else:
                print("YOU LOSE!")
                print(f"Your new balance is ${balance:.2f}")
                print()
                print("-----------------------------------------")



if __name__ == '__main__':
    main()