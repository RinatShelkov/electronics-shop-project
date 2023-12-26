# -*- coding: utf-8 -*-
from src.item import Item


class Mixin:
    """Хранение и изменение языка EN и RU"""

    def __init__(self, language="EN"):
        self.__language = language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """Изменяет язык EN на RU  и наоборот"""
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self


class Keyboard(Item, Mixin):
    """Товар - клавиатура"""

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
