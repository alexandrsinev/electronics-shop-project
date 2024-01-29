import csv
import os
from config import ROOT_DIR




class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []


    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.pay_rate * self.price

    @property
    def name(self):
        """ Возвращает значение названия товара"""

        return self.__name

    @name.setter
    def name(self, name):
        """ Принимает название товара, обрезает название на длинну не больше 10 символов"""

        self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls, f):
        file = os.path.join(ROOT_DIR, f)
        cls.all = []
        with open(file, newline='') as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                cls(row['name'], float(row['price']), int(row['quantity']))

    @staticmethod
    def string_to_number(str_number):
        number = int(float(str_number))
        return number


