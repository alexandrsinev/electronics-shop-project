import csv
import os
from config import ROOT_DIR


class InstantiateCSVError(Exception):
    def __init__(self):
        self.message = 'InstantiateCSVError: Файл item.csv поврежден'



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
        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        """
        Метод производит сложение количества товара
        """

        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        else:
            return self.quantity + other.quantity

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
        try:
            file = os.path.join(ROOT_DIR, f)
            cls.all = []
            with open(file, newline='') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    if row['name'] is None or row['price'] is None or row['quantity'] is None:
                        raise InstantiateCSVError
                    else:
                        cls(row['name'], float(row['price']), int(row['quantity']))
        except InstantiateCSVError as e:
            print(e.message)
            raise InstantiateCSVError

        except FileNotFoundError:
            print('FileNotFoundError: Отсутствует файл item.csv')


    @staticmethod
    def string_to_number(str_number):
        number = int(float(str_number))
        return number

# Item.instantiate_from_csv('src/items.csv')
