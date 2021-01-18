import pytest

class Checkout:
    class Discout:
        def __init__(self, nbrItems, price):
            self.nbrItems = nbrItems
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}
        self.total = 0

    def addDiscount(self, item, nbrOfItems, price):
        discount = self.Discout(nbrOfItems, price)
        self.discounts[item] = discount

    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculateTotal(self):
        total = 0
        for item, cnt in self.items.items():
            total += self.calculateItemTotal(item, cnt)
        return total

    def calculateItemTotal(self, item, cnt):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if cnt >= discount.nbrItems:
                nbrOfDiscounts = cnt/discount.nbrItems
                total += nbrOfDiscounts * discount.price
                remaining  = cnt % discount.nbrItems
                total += remaining * self.prices[item]
            else:
                total += self.prices[item] * cnt
        else:
            total += self.prices[item] * cnt

        return total
