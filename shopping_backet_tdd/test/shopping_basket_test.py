from dataclasses import dataclass
from typing import List
from unittest import TestCase


@dataclass
class Item:
    unit_price: float
    quantity: int


@dataclass
class ShoppingBasket:
    items: List[Item]

    def __init__(self):
        self.items = []

    def get_total_value(self):
        if len(self.items) > 0:
            return self.calculate_total()
        return 0

    def calculate_total(self):
        total: float = 0
        for item in self.items:
            total += item.unit_price * item.quantity
        return total

    def add_item(self, item):
        self.items.append(item)


class ShoppingBasketTest(TestCase):

    def test_calculate_total_for_empty_basket(self):
        basket = ShoppingBasket()

        self.assertEquals(0, basket.get_total_value())

    def test_calculate_total_for_backet_with_one_item(self):
        # Given
        item = Item(10.0, 1)
        basket = ShoppingBasket()

        # When
        basket.add_item(item)

        # Then
        self.assertEquals(10.0, basket.get_total_value())

    def test_calculate_total_for_backet_with_two_item(self):
        # Given
        item = Item(10.0, 1)
        item2 = Item(20.0, 1)
        basket = ShoppingBasket()

        # When
        basket.add_item(item)
        basket.add_item(item2)

        # Then
        self.assertEquals(30.0, basket.get_total_value())

    def test_calculate_total_for_backet_with_multiple_items_multiple_quantities(self):
        # Given
        item = Item(10.0, 5)
        item2 = Item(20.0, 5)
        basket = ShoppingBasket()

        # When
        basket.add_item(item)
        basket.add_item(item2)

        # Then
        self.assertEquals(150.0, basket.get_total_value())
