import os
import time


menu = {
    'espresso': {
        'ingredients': {'water': 50, 'coffee': 18, 'milk': 0},
        'cost': 1.5,
        },
    'latte': {
        'ingredients': {'water': 200, 'coffee': 24, 'milk': 150},
        'cost': 2.5
    },
    'cappuccino': {
        'ingredients': {'water': 250, 'coffee': 24, 'milk': 100},
        'cost': 3.0
    }
}

# print(menu)

# Coffee machine stock capacity of ingredients
machine_has = {
    'ingredients': {'water': 1000, 'coffee': 200, 'milk': 500},
    'balance': 0
    }

# Get a report about coffee machine capacity
def print_report():

    print(f'\tWater: {machine_has["ingredients"]["water"]}ml')
    print(f'\tCoffee: {machine_has["ingredients"]["coffee"]}gr')
    print(f'\tMilk: {machine_has["ingredients"]["milk"]}ml')
    print(f'\tMoney: ${machine_has["balance"]}')
    print()


# # Coins in USD which coffee machine can take
# coins = {
#     'penny': 0.01,
#     'nickel': 0.05,
#     'dime': 0.1,
#     'quarter': 0.25
# }

def has_sufficient_stock(coffee):
    """Check if the coffee machine has sufficient stock
    to make a coffee from an order."""
    machine = [*machine_has['ingredients'].values()]
    order = [*menu[coffee]['ingredients'].values()]
    for x in range(0, len(machine)):
        if machine[x] - order[x] < 0:
            return False
    return True


def process_coin(coffee):
    """Count every coin user put inside,
    subtract coffee cost and give a change back to user."""
    quarters = int(input('How many quarters?: '))*0.25
    dimes = int(input('How many dimes?: '))*0.1
    nickels = int(input('How many nickels?: '))*0.05
    pennies = int(input('How many pennies?: '))*0.01
    total = round((quarters + dimes + nickels + pennies),2)
    # print(total)
    coffee_cost = menu[coffee]['cost']
    # print(coffee_cost)
    if check_transaction(total, coffee_cost):
        make_coffee(coffee)



def check_transaction(total, cost):
    """Check if user put enough money. If not, they got a refund."""
    delta = round((total - cost),2)
    if delta > 0:
        print(f'Here is ${delta} in change.')
        return True
    elif delta == 0:
        print(f'Here is no money in change.')
        return True
    else:
        print('Sorry, that\'s not enough money. Money refunded.')
        return False

def make_coffee(coffee):
    """Make coffee. All ingredients used will be subtracted from machine stock.
    Coffee cost will be added to machine balance."""
    global machine_has
    ingredients = [*machine_has['ingredients'].keys()]
    for x in range(0, len(ingredients)):
        machine_has['ingredients'][ingredients[x]] -= menu[coffee]['ingredients'][ingredients[x]]
    machine_has['balance'] += menu[coffee]['cost']
    time.sleep(1)
    print(f'Here is your {coffee} ☕. Enjoy!')


def main():
    user_input = ''
    while user_input != 'quit':
        os.system('cls')
        user_input = input('What would you like? (espresso/latte/cappuccino) or (report/quit): ').lower()
        if user_input in [*menu.keys()]:
            if has_sufficient_stock(user_input):
                process_coin(user_input)
            else:
                print('...sorry, coffee machine needs maintenance')

        elif user_input == 'report':
            print_report()
        try:
            input("Press [enter] to continue...")
        except SyntaxError:
            pass
    os.system('cls')
    print('...ok, here is the final report: ')
    print_report()


if __name__ == '__main__':
    main()
