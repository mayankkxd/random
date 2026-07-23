def take():
    cart = {}
    while True:
        print("Enter an item and its price: (q to stop) ")
        item = input().lower()
        if item.isalpha():
            if item == 'q':
                break
            else:
                try:
                    price = float(input())
                except ValueError:
                    print("---------------------")
                    print("Please re-enter item with correct price.")
                    print("---------------------")
                    continue
                cart.update({item.capitalize(): price})
        else:
            print("---------------------")
            print("Item must contain only alphabets. Re-enter item.")
            print("---------------------")
            continue
    return cart 

def calc(cart):
    cost = 0
    for value in cart.values():
        cost += value
    return cost

def layout():
    print("****************************")
    print("Welcome to the shop.")
    print("****************************")

def showresult(cart, total):
    print("Your shopping bag is: ")
    for key, value in cart.items():
        print(f"{key}:\t{value}/-")
    print("Your total is: ", total)

def main():
    layout()
    cart = take()
    total = calc(cart)
    showresult(cart, total)

if __name__ == '__main__':
    main()