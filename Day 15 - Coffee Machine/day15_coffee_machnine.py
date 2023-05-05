report = """Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0"""

while True:
    choice = input('What would you like? (espresso/latte/cappucino): ')

    if choice == 'report':
        print(report)
        