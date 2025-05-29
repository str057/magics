import pytest
from src.main import (
    Product,
    Category,
)  # Импортируйте из вашего файла, если он называется иначе, замените


def test_product_str():
    product = Product("TestProduct", "Desc", 100.0, 3)
    assert str(product) == "TestProduct, 100.0 руб. Остаток: 3 шт."


def test_category_str():
    p1 = Product("P1", "desc", 10.0, 5)
    p2 = Product("P2", "desc", 20.0, 10)
    category = Category("TestCategory", "desc", [p1, p2])
    assert str(category) == "TestCategory, количество продуктов: 15 шт."


def test_product_add():
    p1 = Product("P1", "desc", 10.0, 5)
    p2 = Product("P2", "desc", 20.0, 10)
    assert p1 + p2 == (10.0 * 5 + 20.0 * 10)
