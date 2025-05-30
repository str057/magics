import pytest
from src.main import (
    Product,
    Category,
)  # Импортируйте из вашего файла, если он называется иначе, замените


def test_product_str():
    product = Product("Test", "Description", 100, 5)
    assert str(product) == "Test, 100 руб. Остаток: 5 шт."


def test_category_str():
    products = [Product("Test1", "Desc1", 100, 2), Product("Test2", "Desc2", 200, 3)]
    category = Category("TestCat", "TestDesc", products)
    assert "Категория: TestCat" in str(category)
    assert "Количество продуктов: 5 шт." in str(category)


def test_product_addition():
    p1 = Product("P1", "Desc", 10, 2)
    p2 = Product("P2", "Desc", 20, 3)
    assert p1 + p2 == 80


def test_product_addition_invalid_type():
    p1 = Product("P1", "Desc", 10, 2)
    with pytest.raises(TypeError):
        p1 + 100
