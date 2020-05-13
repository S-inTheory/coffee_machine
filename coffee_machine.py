money = 550
water = 400
milk = 540
coffee_bean = 120
cups = 9


class CoffeeMachine:
    def action(self):
        while True:
            print('Write action (buy, fill, take, remaining, exit):')
            action = input()
            if action == 'buy':
                buy()
                continue
            elif action == 'fill':
                fill()
                continue
            elif action == 'take':
                take()
                continue
            elif action == 'remaining':
                print('The coffee machine has:')
                print(f'{water} of water')
                print(f'{milk} of milk')
                print(f'{coffee_bean} of coffee beans')
                print(f'{cups} of disposable cups')
                print(f'{money} of money')
                continue
            elif action == 'exit':
                break


def buy():
    global water
    global milk
    global coffee_bean
    global cups
    global money
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
    while True:
        coffee = input()
        if coffee == '1':
            if water < 250:
                print('Sorry, not enough water!')
                break
            water = water - 250
            if coffee_bean < 16:
                print('Sorry, not enough coffee bean!')
                break
            coffee_bean = coffee_bean - 16
            if cups < 1:
                print('Sorry, not enough cups!')
                break
            cups = cups - 1
            print('I have enough resources, making you a coffee!')
            money = money + 4
            break

        elif coffee == '2':
            if water < 350:
                print('Sorry, not enough water!')
                break
            water = water - 350
            if milk < 75:
                print('Sorry, not enough milk!')
                break
            milk = milk - 75
            if coffee_bean < 20:
                print('Sorry, not enough coffee bean!')
                break
            coffee_bean = coffee_bean - 20
            if cups < 1:
                print('Sorry, not enough cups!')
                break
            cups = cups - 1
            print('I have enough resources, making you a coffee!')
            money = money + 7
            break
        elif coffee == '3':
            if water < 200:
                print('Sorry, not enough water!')
                break
            water = water - 200
            if milk < 100:
                print('Sorry, not enough milk!')
                break
            milk = milk - 100
            if coffee_bean < 12:
                print('Sorry, not enough coffee bean!')
                break
            coffee_bean = coffee_bean - 12
            if cups < 1:
                print('Sorry, not enough cups!')
                break
            cups = cups - 1
            print('I have enough resources, making you a coffee!')
            money = money + 6
            break
        elif coffee == 'back':
            break


def fill():
    global water
    global milk
    global coffee_bean
    global cups
    global money
    print('Write how many ml of water do you want to add:')
    water_fill = int(input())
    water = water + water_fill
    print('Write how many ml of milk do you want to add:')
    milk_fill = int(input())
    milk = milk + milk_fill
    print('Write how many grams of coffee beans do you want to add:')
    coffee_bean_fill = int(input())
    coffee_bean = coffee_bean + coffee_bean_fill
    print('Write how many disposable cups of coffee do you want to add:')
    cups_fill = int(input())
    cups = cups + cups_fill


def take():
    global water
    global milk
    global coffee_bean
    global cups
    global money
    print(f'I gave you ${money}')
    money = 0


coffee_machine = CoffeeMachine()

coffee_machine.action()
