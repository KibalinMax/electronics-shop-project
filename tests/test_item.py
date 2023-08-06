"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

def test_calculate_total_price():
    item_pr_1 = Item("Iphone", 100000, 10)
    total_price = item_pr_1.calculate_total_price()
    assert total_price == 1000000

def test_item_apply_discount():
    item_pr_2 = Item("Honor", 20000, 20)
    item_pr_2.pay_rate = 0.5
    item_pr_2.apply_discount()
    assert item_pr_2.price == 10000
