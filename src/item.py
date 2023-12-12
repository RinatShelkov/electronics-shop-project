import csv
import re

from data.config import ROOT_PATH


class Item:
    """
    Класс для представления товара в магазине.
    """

    pay_rate = 1
    all = []

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

        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    @property
    def name(self):
        Item.all.append(self)
        return self.__name

    @name.setter
    def name(self, name):
        Item.all.append(self)
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[0:10]

    @classmethod
    def instantiate_from_csv(cls, file_csv):
        Item.all.append(cls)
        with open(ROOT_PATH.joinpath(file_csv), newline="") as csvfile:
            results = csv.DictReader(csvfile)
            for result in results:
                print(result["name"], result["price"], result["quantity"])

    @staticmethod
    def string_to_number(number_string):
        number = int(re.findall(r"\d+", number_string)[0])
        return number

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """

        return self.price * self.quantity

    def apply_discount(self) -> None | float:
        """
        Применяет установленную скидку для конкретного товара.
        """

        self.price = self.price * Item.pay_rate
        return self.price
