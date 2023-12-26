"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def item_1():
    item1 = Item("Смартфон", 10000, 20)
    return item1


@pytest.fixture
def phone_1():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    return phone1


@pytest.fixture
def unknow_class():
    class Unknow:
        """
        Класс для теста.
        """

        def __init__(self, name: str, price: float, quantity: int) -> None:
            """
            Создание экземпляра класса item.

            :param name: Название товара.
            :param price: Цена за единицу товара.
            :param quantity: Количество товара в магазине.
            """
            self.__name = name
            self.price = price
            self.quantity = quantity

        def __add__(self, other):
            if isinstance(other, Item):
                return self.quantity + other.quantity
            raise TypeError("Складывать можно только объекты классов с родительским классом Item")

    unknow_class = Unknow("Смартфон", 10000, 20)
    return unknow_class


def test_item_homework_1(item_1):
    # Проверка calculate_total_price - получение общей стоимости конкретного товара в магазине
    assert item_1.calculate_total_price() == 200000

    # Проверка изменения размера скидке в классе
    Item.pay_rate = 0.8
    assert Item.pay_rate == 0.8

    # Проверка apply_discount() - применнение скидки для товара
    assert item_1.apply_discount() == 8000.0

    # Проверка сколько экземпляров класса создано
    assert len(item_1.all) == 1

    # Проверка изменения наименования с декоратором property и setr, длина слова до 10 символов
    item_1.name = "Смартфон"
    assert item_1.name == "Смартфон"

    # Проверка изменения наименования с декоратором property и setr, длина слова больше 10 символов,
    # обрезает  строку (оставляет первые 10 символов)
    item_1.name = "Смартфон123456"
    assert item_1.name == "Смартфон12"

    # проверка string_to_number()` - статический метод, возвращающий число из числа-строки
    assert Item.string_to_number("5") == 5

    # Проверка работоспобоности @classmethod


def test_from_csv(capsys):
    Item.instantiate_from_csv("src/items.csv")
    log_text = capsys.readouterr()
    assert log_text.out.strip() == "Смартфон 100 1\nНоутбук 1000 3\nКабель 10 5\nМышка 50 5\nКлавиатура 75 5"

    # Проверка работоспособности __repr__ и __str__


def test_repr_str(item_1):
    assert repr(item_1) == "Item('Смартфон', 10000, 20)"
    assert str(item_1) == "Смартфон"


def test_add(item_1, phone_1, unknow_class):
    assert item_1 + phone_1 == 25
    assert phone_1 + phone_1 == 10

    with pytest.raises(TypeError):
        phone_1 + unknow_class
