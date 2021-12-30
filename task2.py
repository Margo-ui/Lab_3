import json
import datetime


class Pizza:
    with open("pizza.json") as pizzafile:
        data_of_pizza = json.load(pizzafile)

    def print_pizza(self):
        if self.day == "Invalid":
            return
        print("Pizza for " + self.day + ": " + str(Pizza.data_of_pizza[self.day]["name"]))
        print(str(Pizza.data_of_pizza[self.day]["ingridients"]) + str(self.ingridients) + " " + str(
            Pizza.data_of_pizza[self.day]["price"]))

    def __init__(self, ingridients):
        self.ingridients = list()
        if not isinstance(ingridients, list):
            return
        self.ingridients += ingridients


class Pizza_Monday(Pizza):
    def __init__(self, ingridients):
        super().__init__(ingridients)
        self.day = "Monday"


class Pizza_Tuesday(Pizza):
    def __init__(self, ingridients):
        super().__init__(ingridients)
        self.day = "Tuesday"


class Pizza_Wednesday(Pizza):
    def __init__(self, ingridients):
        super().__init__(ingridients)
        self.day = "Wednesday"


class Pizza_Thursday(Pizza):
    def __init__(self, ingridients):
        super().__init__(ingridients)
        self.day = "Thursday"


class Pizza_Friday(Pizza):
    def __init__(self, ingridients):
        super().__init__(ingridients)
        self.day = "Friday"


class Pizza_Saturday(Pizza):
    def __init__(self, ingridients):
        super().__init__(ingridients)
        self.day = "Saturday"


class Pizza_Sunday(Pizza):
    def __init__(self, ingridients):
        super().__init__(ingridients)
        self.day = "Sunday"


class Pizza_Invalid(Pizza):
    def __init__(self, ingridients):
        super().__init__(ingridients)
        self.day = "Invalid"


def order(ingridients=[], day=None):
    if not isinstance(ingridients, list):
        ingridients = list()
    make_pizza = None
    if day is None:
        day = datetime.date.today().weekday()
    if day == 0:
        make_pizza = Pizza_Monday(ingridients)
    elif day == 1:
        make_pizza = Pizza_Tuesday(ingridients)
    elif day == 2:
        make_pizza = Pizza_Wednesday(ingridients)
    elif day == 3:
        make_pizza = Pizza_Thursday(ingridients)
    elif day == 4:
        make_pizza = Pizza_Friday(ingridients)
    elif day == 5:
        make_pizza = Pizza_Saturday(ingridients)
    elif day == 6:
        make_pizza = Pizza_Sunday(ingridients)
    else:
        print("Incorrect day")
        make_pizza = Pizza_Invalid(ingridients)
    return make_pizza


order(["something", "smth"]).print_pizza()
order(["some", "smth"], 1).print_pizza()
order(["some1", "smth"], 2).print_pizza()
order(["some2", "smth"], 0).print_pizza()
order(["some3", "smth"], 4).print_pizza()
order().print_pizza()
order(["some3", "smth"], 5).print_pizza()
order(["some3", "smth"], 6).print_pizza()
order(["some3", "smth"], 10).print_pizza()
