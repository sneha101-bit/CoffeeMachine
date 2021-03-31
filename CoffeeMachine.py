class CoffeeMachine:
    options = ['buy', 'fill', 'take', 'remaining', 'exit']
    coffee_type = ['espresso', 'latte', 'cappuccino', 'back - to main menu']

    def __init__(self):
        self.WATER = 400
        self.MILK = 540
        self.COFFEE = 120
        self.no_disposable_cups = 9
        self.money = 550
        self.fill_water = 0
        self.fill_milk = 0
        self.fill_coffee = 0
        self.fill_disposable_cup = 0
        self.avail_water = 0
        self.avail_coffee = 0
        self.avail_milk = 0
        self.coffee_index = 0

    def looping_actions(self):

        index = ''
        list_index = []
        while index != 'exit':
            index = input("Write action (buy, fill, take, remaining, exit):")
            list_index.append(index)
            if index == 'buy':

                coffee_index = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")

                if coffee_index == '1' and self.WATER >= 250 and self.COFFEE >= 16:
                    self.water_needs = 250
                    self.coffee_needs = 16
                    self.milk_needs = 0
                    self.WATER = self.WATER - self.water_needs
                    self.COFFEE = self.COFFEE - self.coffee_needs
                    self.MILK = self.MILK - self.milk_needs
                    self.no_disposable_cups = self.no_disposable_cups - 1
                    self.money = self.money + 4
                    print("I have enough resources, making you a coffee!")
                elif coffee_index == '1' and self.WATER < 250 and self.COFFEE >= 16:
                    print("Sorry, not enough water!")
                elif coffee_index == '1' and self.WATER >= 250 and self.COFFEE < 16:
                    print("Sorry, not enough coffee!")

                elif coffee_index == '2' and self.WATER >= 350 and self.COFFEE >= 20 and self.MILK >= 75:
                    self.water_needs = 350
                    self.coffee_needs = 20
                    self.milk_needs = 75
                    self.WATER = self.WATER - self.water_needs
                    self.COFFEE = self.COFFEE - self.coffee_needs
                    self.MILK = self.MILK - self.milk_needs
                    self.no_disposable_cups = self.no_disposable_cups - 1
                    self.money = self.money + 7
                    print("I have enough resources, making you a coffee!")
                elif coffee_index == '2' and self.WATER < 350 and self.COFFEE >= 20:
                    print("Sorry, not enough water!")
                elif coffee_index == '2' and self.WATER >= 350 and self.COFFEE < 20:
                    print("Sorry, not enough coffee!")

                elif coffee_index == '3' and self.WATER >= 200 and self.COFFEE >= 12 and self.MILK >= 100:
                    self.water_needs = 200
                    self.coffee_needs = 12
                    self.milk_needs = 100
                    self.WATER = self.WATER - self.water_needs
                    self.COFFEE = self.COFFEE - self.coffee_needs
                    self.MILK = self.MILK - self.milk_needs
                    self.no_disposable_cups = self.no_disposable_cups - 1
                    self.money = self.money + 6
                    print("I have enough resources, making you a coffee!")
                elif coffee_index == '3' and self.WATER < 200 and self.COFFEE >= 12 and self.MILK >= 100:
                    print("Sorry, not enough water!")
                elif coffee_index == '3' and self.WATER >= 200 and self.COFFEE < 12 and self.MILK >= 100:
                    print("Sorry, not enough coffee!")
                elif coffee_index == '3' and self.WATER >= 200 and self.COFFEE >= 12 and self.MILK < 100:
                    print("Sorry, not enough milk!")

                elif coffee_index == '4':
                    return CoffeeMachine.looping_actions(self)

            elif index == 'fill':
                self.fill_water = int(input("Write how many ml of water do you want to add:"))
                self.fill_milk = int(input("Write how many ml of milk do you want to add:"))
                self.fill_coffee = int(input("Write how many grams of coffee beans do you want to add:"))
                self.fill_disposable_cup = int(input("Write how many disposable cups of coffee do you want to add:"))
                self.WATER = self.WATER + self.fill_water
                self.COFFEE = self.COFFEE + self.fill_coffee
                self.MILK = self.MILK + self.fill_milk
                self.no_disposable_cups = self.no_disposable_cups + self.fill_disposable_cup

            elif index == 'take':
                self.WATER = self.WATER
                self.COFFEE = self.COFFEE
                self.MILK = self.MILK
                self.no_disposable_cups = self.no_disposable_cups
                print("I gave you ${}".format(self.money))
                self.money = self.money - self.money

            elif index == 'remaining':
                previous_action = list_index[-1]
                if previous_action == 'buy':
                    if self.coffee_index == '1' and self.WATER >= 250 and self.COFFEE >= 16:
                        print("""
                        The coffee machine has:
                        {} of water
                        {} of milk
                        {} of coffee beans
                        {} of disposable cups
                        {} of money
                        """.format(self.WATER, self.MILK, self.COFFEE, self.no_disposable_cups, self.money))

                    elif self.coffee_index == '2' and self.WATER >= 350 and self.COFFEE >= 20 and self.MILK >= 75:
                        print("""
                        The coffee machine has:
                        {} of water
                        {} of milk
                        {} of coffee beans
                        {} of disposable cups
                        {} of money
                        """.format(self.WATER, self.MILK, self.COFFEE, self.no_disposable_cups, self.money))

                    elif self.coffee_index == '3' and self.WATER >= 200 and self.COFFEE >= 12 and self.MILK >= 100:
                        print("""
                        The coffee machine has:
                        {} of water
                        {} of milk  
                        {} of coffee beans
                        {} of disposable cups
                        {} of money
                        """.format(self.WATER, self.MILK, self.COFFEE, self.no_disposable_cups, self.money))

                elif previous_action == 'take':
                    self.WATER = self.WATER
                    self.COFFEE = self.COFFEE
                    self.MILK = self.MILK
                    self.no_disposable_cups = self.no_disposable_cups
                    print("""
                    The coffee machine has:
                    {} of water
                    {} of milk
                    {} of coffee beans
                    {} of disposable cups
                    {} of money
                    """.format(self.WATER, self.MILK, self.COFFEE, self.no_disposable_cups, self.money))

                elif previous_action == 'fill':
                    print("""
                    The coffee machine has:
                    {} of water
                    {} of milk
                    {} of coffee beans
                    {} of disposable cups
                    {} of money
                    """.format(self.WATER, self.MILK, self.COFFEE, self.no_disposable_cups, self.money))

                elif previous_action == 'remaining':
                    self.WATER = self.WATER
                    self.COFFEE = self.COFFEE
                    self.MILK = self.MILK
                    self.no_disposable_cups = self.no_disposable_cups
                    print("""
                    The coffee machine has:
                    {} of water
                    {} of milk
                    {} of coffee beans
                    {} of disposable cups
                    {} of money""".format(self.WATER, self.MILK, self.COFFEE, self.no_disposable_cups, self.money))

            elif index == 'exit':
                exit()
                break

actions = CoffeeMachine()
actions.looping_actions()
