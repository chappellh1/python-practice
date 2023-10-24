def main():
    printMenu()
    bare_Price = combos()
    taxxedprice = subtotalandtax(bare_Price)
    tip = getTip(taxxedprice)
    Total = calcfinaltotal(tip, taxxedprice)
    print("your total is: $", Total)

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

def combos():
    selected_items = []
    price = 0
    comboMenu = {
        "1": "beans and califlower: $2000.00",
        "2": "cauliflower and bread: $101.00",
        "3": "bread and pork: $21.00",
        "4": "pork and chicken: $20",
        "5": "chicken and beans: $250"
    }
    while True:
            for key, value in comboMenu.items():
                print(f"{key}: {value}")
        
            comboChoice = input("Please select a combo item (or type 'done' to finish): ")

            if comboChoice in comboMenu:
                selected_items.append(comboChoice)
                price += float(comboMenu[comboChoice].split('$')[1])  # Extract the price and add to total
                print(f"You selected {comboMenu[comboChoice]}")

            elif comboChoice.lower() == 'done':
                break
            print("Selected items:")
            for item in selected_items:
                print(comboMenu[item])

    return price


def subtotalandtax(price):

    tax = price * .10 #10% tax
    print("tax is:", tax)
    totalprice = tax + price
    return totalprice

def getTip(totalprice):
    tipChoices = { # selecting tip percentage of meal
        "1": "10%",
        "2": "12%",
        "3": "14%",
        "4": "16%",
        "5": "20%",
    }
    while True:
            print("Tip Choices:")
            for key, value in tipChoices.items():
                print(f"{key}: {value}")

            tip_choice = input("Please select a tip percentage (1-5): ")

            if tip_choice in tipChoices:
                tip_percentage = [0.10, 0.12, 0.14, 0.16, 0.20][int(tip_choice) - 1]
                tip = totalprice * tip_percentage
                return tip

       

def calcfinaltotal(tip,totalprice):
    finalTotal = tip + totalprice
    return finalTotal


    
if __name__ == "__main__":
    main()