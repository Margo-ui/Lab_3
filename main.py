# Write a program for selling tickets to IT-events. Each ticket has a unique
# number and a price. There are four types of tickets: regular ticket,
# advance ticket (purchased 60 or more days before the event), late ticket
# (purchased fewer than 10 days before the event) and student ticket.
# Additional information:
# -advance ticket - discount 40% of the regular ticket price;
# -student ticket - discount 50% of the regular ticket price;
# -late ticket - additional 10% to the regular ticket price.
# All tickets must have the following properties:
# -the ability to construct a ticket by number;
# -the ability to ask for a ticket’s price;
# -the ability to print a ticket as a String.


from typing import Type
from constants_for_task1 import LATE, REGULAR, ADVANCE, STUDENT, TICKETS_JSON, SOLD_TICKETS_JSON

import json
from datetime import date


class Ticket:
    """
    Ticket class. Gets ticket information from a JSON-file.
    """

    _id = 0
    dict_of_tickets = {}

    with open(TICKETS_JSON) as tickets:
        data_of_tickets = json.load(tickets)

    def __init__(self, name_event, type_ticket):
        self._id = Ticket._id
        self._name_event = name_event
        self._date_of_event = Ticket.data_of_tickets[name_event]['date']

        Ticket._id += 1
        Ticket.update_data(self, name_event, type_ticket)
        Ticket.sold_data(self, name_event, type_ticket)

    def __str__(self):
        return f"""
    Price of ticket: {Ticket.data_of_tickets[self._name_event]['price']}$
    Name of event: {self._name_event}
    Date of event: {self._date_of_event}
    """

    def update_data(self, name_event, type_ticket):
        Ticket.data_of_tickets[name_event][type_ticket] -= 1
        with open(TICKETS_JSON, 'w') as update_tickets:
            update_tickets.write(json.dumps(Ticket.data_of_tickets, indent=4))

    def sold_data(self, name_event, type_ticket):
        with open(SOLD_TICKETS_JSON, 'w') as sold_tickets:
            Ticket.dict_of_tickets[Ticket._id] = {
                "name_event": f'{name_event}',
                "date": Ticket.data_of_tickets[name_event]['date'],
                "type": type_ticket,
                "price": Ticket.data_of_tickets[name_event]['price']
            }

            data = json.dumps(Ticket.dict_of_tickets,
                              indent=4, separators=(',', ': '))
            sold_tickets.write(data)


class Regular(Ticket):
    type_ticket = 'regular'

    def __init__(self, name_event):
        today = date.today()
        int_date = [
            int(item) for item in Ticket.data_of_tickets[name_event]['date'].split('.')]
        days_to_event = date(int_date[2], int_date[1], int_date[0]) - today
        if days_to_event.days < 0:
            raise ValueError('Choose other type of ticket')

        if not Ticket.data_of_tickets[name_event][Regular.type_ticket]:
            raise ValueError('There are no such type tickets left')

        super().__init__(name_event, Regular.type_ticket)

        self.price = Ticket.data_of_tickets[name_event]['price']

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            raise ValueError('Price of ticket must be > 0')
        self.__price = price * REGULAR


class Advance(Ticket):
    type_ticket = 'advance'

    def __init__(self, name_event):
        today = date.today()
        int_date = [
            int(item) for item in Ticket.data_of_tickets[name_event]['date'].split('.')]
        days_to_event = date(int_date[2], int_date[1], int_date[0]) - today
        if days_to_event.days <= 60:
            raise ValueError(
                'Choose other type of ticket! Less than 60 days before the event.')

        if not Ticket.data_of_tickets[name_event][Advance.type_ticket]:
            raise ValueError('There are no such type tickets left')

        super().__init__(name_event, Advance.type_ticket)
        self.price = Ticket.data_of_tickets[name_event]['price']

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            raise ValueError('Price of ticket must be > 0')
        self.__price = price * ADVANCE


class Late(Ticket):
    type_ticket = 'late'

    def __init__(self, name_event):
        today = date.today()
        int_date = [
            int(item) for item in Ticket.data_of_tickets[name_event]['date'].split('.')]
        days_to_event = date(int_date[2], int_date[1], int_date[0]) - today
        if not days_to_event.days <= 10:
            raise ValueError(
                'Choose other type of ticket! More than 10 days before the event.')

        if not Ticket.data_of_tickets[name_event][Late.type_ticket]:
            raise ValueError('There are no such type tickets left')

        super().__init__(name_event, Late.type_ticket)
        self.price = Ticket.data_of_tickets[name_event]['price']

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            raise ValueError('Price of ticket must be > 0')
        self.__price = price * LATE


class Student(Ticket):
    type_ticket = 'student'

    def __init__(self, name_event):
        today = date.today()
        int_date = [
            int(item) for item in Ticket.data_of_tickets[name_event]['date'].split('.')]
        days_to_event = date(int_date[2], int_date[1], int_date[0]) - today
        if days_to_event.days < 0:
            raise ValueError('Choose other type of ticket')

        if not Ticket.data_of_tickets[name_event][Student.type_ticket]:
            raise ValueError('There are no such type tickets left')

        super().__init__(name_event, Student.type_ticket)
        self.price = Ticket.data_of_tickets[name_event]['price']

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            raise ValueError('Price of ticket must be > 0')
        self.__price = price * STUDENT


class Customer:
    """
    Class Customer, who can place an order.
    """

    def __init__(self, name, surname, phone_number, student=False):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.__student = student

    def check_input_data(self, input_data):
        if not isinstance(input_data, str):
            raise TypeError('Invalid input data type')
        if not len(input_data):
            raise ValueError('Incorrect data input values')

    @property
    def name(self):
        return self.__name

    @property
    def phone_number(self):
        return self.__phone_number

    @property
    def surname(self):
        return self.__surname

    @property
    def student(self):
        return self.__student

    @name.setter
    def name(self, name):
        self.check_input_data(name)
        self.__name = name

    @surname.setter
    def surname(self, surname):
        self.check_input_data(surname)
        self.__surname = surname

    @phone_number.setter
    def phone_number(self, phone_number):
        if not isinstance(phone_number, str):
            raise TypeError('Invalid input data type')
        if len(phone_number) < 10:
            raise ValueError('Incorrect data input values')
        self.__phone_number = phone_number

    @student.setter
    def student(self, student):
        if not isinstance(student, bool):
            raise TypeError('Invalid input data type')
        self.__student = student

    def __str__(self):
        return f'Customer info: {self.name} {self.surname}, + {self.phone_number}'


class Order:
    """
    Order class. Gets customer information.
    """

    def __init__(self, customer, ticket):
        if not isinstance(customer, Customer) or not isinstance(ticket, Ticket):
            raise TypeError(
                'Incorrect type of input data (Customer or Ticket)')
        if ticket.type_ticket == 'student' and not customer.student:
            raise TypeError('You can not order student type ticket')
        self.__customer = customer
        self.__ticket = ticket
        self.__order_time = date.today()

    @property
    def customer(self):
        return self.__customer

    @property
    def ticket(self):
        return self.__ticket

    @property
    def order_time(self):
        return self.__order_time

    def __str__(self):
        return f"""
    Оrder description:
    Date of order: {self.__order_time}
    {self.__customer}
    {self.__ticket}
    Type of ticket: {self.__ticket.type_ticket}
    Price of order: {self.__ticket.price}$
------------------------------\n"""

    def find_by_id(self, id):
        if not isinstance(id, int):
            raise TypeError('Id type must be integer number')
        if not Ticket.dict_of_tickets.get(id):
            raise KeyError('There is no ticket with such id')

        ticket = Ticket.dict_of_tickets.get(id)

        return f"""
    Name of event: {ticket['name_event']}
    Date of event: {ticket['date']}
    Price of ticket: {ticket['price']}$
    Type of ticket: {ticket['type']}
        """


it_event1 = Late('Event_1')
it_event2 = Late('Event_2')
it_event3 = Advance('Event_3')
it_event4 = Regular('Event_3')

customer1 = Customer('Margo', 'Isachenko', '0665127894', True)
customer2 = Customer('Penny', 'Cooper', '0954813729')

order1 = Order(customer1, it_event1)
order2 = Order(customer1, it_event3)
order3 = Order(customer2, it_event4)

print(order3.find_by_id(1))

print(it_event1)
print(it_event1.price)
print(it_event2)
print(it_event2.price)
print(it_event3)
print(it_event3.price)
print(it_event4)
print(it_event4.price)

print(order1)
print(order2)
print(order3)