"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def item1():
    return Item('Смартфон', 10000, 20)


@pytest.fixture
def item2():
    return Item("Ноутбук", 20000, 5)



def test_total_price1(item1):
    """Проверяем значение возвращаемое методом calculate_total_price для экземпляра item1"""
    assert item1.calculate_total_price() == 200000


def test_total_price2(item2):
    """Проверяем значение возвращаемое методом calculate_total_price для экземпляра item2"""
    assert item2.calculate_total_price() == 100000

def test_name(item1):
    """Проверяем длинну назвния товара"""
    item1.name = 'СуперСмартфон'
    assert len(item1.name) <= 10

def test_instantiate_from_csv():
    """Проверяем длинну назвния товара"""
    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 5

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test_for_repr(item1):
    assert repr(item1) == "Item('Смартфон', 10000, 20)"

def test_for_str(item1):
    assert str(item1) == 'Смартфон'

def test_apply_discount(item1):
    item1.pay_rate = 2
    item1.apply_discount()
    assert item1.price == 20000
