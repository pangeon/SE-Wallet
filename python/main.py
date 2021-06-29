from decimal import Decimal

class Person:
    def __init__(self, name, surname, balance, sms_items = {}):
        self._name = name
        self._surname = surname
        self._balance = balance
        self._sms_items = sms_items

    @property
    def balance(self):
        return self._balance

    @property
    def sms_items(self):
        return self._sms_items

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    @sms_items.setter
    def sms_items(self, sms_items):
        self._sms_items = sms_items

    def add_sms(self, item):
        self.sms_items.update(item)

    def sum_investment(self):
        sum = 0
        for i in self.sms_items.values():
            sum += Decimal(i)
        
        return sum


person = Person("Kamil", "Cecherz", 3000)
person.balance = 4000
person.add_sms({"KGHM": "197.55", "ALCOA": "36.95"})
print(person.balance)
print(person.sms_items["KGHM"])
print(person.sum_investment())



