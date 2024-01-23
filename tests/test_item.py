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
