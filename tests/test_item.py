"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def item_1():
    item1 = Item("Смартфон", 10000, 20)
    return item1


def test_Item_homework_1(item_1):
    assert item_1.calculate_total_price() == 200000
    Item.pay_rate = 0.8
    assert Item.pay_rate == 0.8

    assert item_1.apply_discount() == 8000.0
    assert len(item_1.all) == 1
