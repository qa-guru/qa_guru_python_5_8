"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture()
def cart():
    return Cart()

class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """
    def test_product_check_quantity(self, product):

        # TODO напишите проверки на метод check_quantity

        assert product.check_quantity(999) is True
        assert product.check_quantity(1000) is True
        assert product.check_quantity(0) is True
        assert product.check_quantity(1001) is False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(0)
        assert product.quantity == 1000, "ни один товар не куплен"
        product.buy(1)
        assert product.quantity == 999, "куплен 1 товар, остаток 999 шт."
        product.buy(998)
        assert product.quantity == 1, "куплено 998 товаров, остаток 1 шт."
        product.buy(1)
        assert product.quantity == 0, "куплено 1 товаров, остаток 0 шт."

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            assert product.buy(1001), 'Недостаточно продуктов для покупки'

class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_product(self,cart,product):
        assert len(cart.products) == 0, "Корзина пустая"
        cart.add_product(product)
        assert cart.products[product] == 1 ,"добавлен 1 товар"
        cart.add_product(product, 999)
        assert cart.products[product] == 1000, "добавлено еще 999 товаров"
        assert len(cart.products) == 1

    def test_remove_product(self,cart,product):
        cart.add_product(product, 100)
        cart.remove_product(product, 1)
        assert cart.products[product] == 99, 'в корзине 1 товаров'
        print(cart.products[product])
        cart.remove_product(product)
        print(len(cart.products))
        assert len(cart.products) == 0
        cart.add_product(product, 20)
        cart.remove_product(product,300)
        assert len(cart.products) == 0

    def test_clear (self,cart,product):
        cart.add_product(product,100)
        cart.clear()
        assert len(cart.products) == 0

    def test_get_total_price (self,cart,product):
        cart.add_product(product,100)
        print(cart.products[product])
        assert cart.get_total_price() == 10000

    def test_buy(self,cart,product):
        cart.add_product(product, 100)
        cart.buy()
        assert len(cart.products) == 0
        cart.add_product(product,1)
        with pytest.raises(ValueError):
            assert cart.buy()




