from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    # ВЫзываем переменную в которую поместили значение сим карт
    def number_of_sim(self):
        Item.all.append(self)
        return self.__number_of_sim

    @number_of_sim.setter
    # Проверка  количества сим карт
    def number_of_sim(self, number):
        if number <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")
        self.__number_of_sim = number
