def main():
    printMenu()
    bare_Price = combos()
    taxxedprice = subtotalandtax(bare_Price)
    tip = getTip(taxxedprice)
    Total = calcfinaltotal(tip, taxxedprice)
    

def printMenu():
    menu = {
        "1": "beans: $5.00",
        "2": "cauliflower: $10.00",
        "3": "bread: $25.00",
        "4": "pork: $200",
        "5": "chicken: $1"
    }
    print("Menu:")
    for key, value in menu.items():
        print(f"{key}: {value}")
    print("\nAbove are our base items, please order from the combo menu")

def combos():
    print("\nWelcome to our combo menu, where you can see our base items and combination items.")
    print("As you can see, we have 10 items available\n")

    selected_items = {}  # Use a dictionary to store items and their quantities.
    price = 0

    comboMenu = {
        "1": "beans: $5.00",
        "2": "cauliflower: $10.00",
        "3": "bread: $25.00",
        "4": "pork: $20",
        "5": "chicken: $1",
        "6": "beans and cauliflower: $15.00",
        "7": "cauliflower and bread: $35.00",
        "8": "bread and pork: $45.00",
        "9": "pork and chicken: $21.00",
        "10": "chicken and beans: $6.00"
    }

    while True:
        for key, value in comboMenu.items():
            if key in selected_items:
                print(f"{key}: {value} (Quantity: {selected_items[key]})")
            else:
                print(f"{key}: {value}")

        comboChoice = input("\nPlease select a combo item (or type 'done' to finish): ")

        if comboChoice in comboMenu:
            if comboChoice in selected_items:
                selected_items[comboChoice] += 1
            else:
                selected_items[comboChoice] = 1

            price += float(comboMenu[comboChoice].split('$')[1])
            print(f"You selected {comboMenu[comboChoice]}. Please select the next item or finish")

        elif comboChoice.lower() == 'done':
            break

    print("\nSelected items:")
    for item, quantity in selected_items.items():
        print(f"{comboMenu[item]} (Quantity: {quantity})")

    return price


def subtotalandtax(price):
    taxrate = "10%"
    taxratenum = 0.10
    tax = price * taxratenum
    totalprice = tax + price
    # Use f-strings to format the numbers with two decimal places
    print(f"\nAfter applying the tax rate of {taxrate} to your order price of {price}\nYour tax is: ${tax:.2f}")
    return totalprice

def getTip(totalprice):
    tipChoices = {
        "1": "10%",
        "2": "12%",
        "3": "14%",
        "4": "16%",
        "5": "20%",
    }
    while True:
        print("\nTip Choices:")
        for key, value in tipChoices.items():
            print(f"{key}: {value}")

        tip_choice = input("\nPlease select a tip percentage (1-5): ")

        if tip_choice in tipChoices:
            tip_percentage = [0.10, 0.12, 0.14, 0.16, 0.20][int(tip_choice) - 1]
            print(f"\nyou selected a tip percentages of: {tip_percentage}%")
            tip = totalprice * tip_percentage
            print (f"\nSince your meal price was: ${totalprice} your tip is: ${tip:.2f}\n")
            return tip

def calcfinaltotal(tip, totalprice):
    finalTotal = tip + totalprice
    print(f"Calculating your total with your tip. Your tip is: ${tip:.2f} adding it to the price of the meal with tax applied"),
    print(f"that was: ${totalprice} Your final price is: ${finalTotal:.2f}")
    return finalTotal

if __name__ == "__main__":
    main()