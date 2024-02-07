from src.item import Item


class ChangeLang:
    """Kласс-миксин. Реализует дополнительный функционал по хранению и изменению раскладки клавиатуры"""

    def __init__(self, language='EN'):
        self.__language = language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
            return self.__language
        elif self.__language == 'RU':
            self.__language = 'EN'
            return self.__language

    @property
    def language(self):

        return self.__language


class Keyboard(Item, ChangeLang):
    """Класс для создания экземпляров - клавиатуры"""
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)

    def __str__(self):
        return self.name
