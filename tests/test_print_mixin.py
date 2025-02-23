import pytest

from src.print_mixin import PrintMixin


def test_repr_with_all_attributes(product_1):
    expected_repr = 'Product(55" QLED 4K, Фоновая подсветка, 123000.0, 7)'
    assert repr(product_1) == expected_repr


def test_repr_with_missing_attributes():
    class IncompleteProduct(PrintMixin):
        def __init__(self, name: str):
            self.name = name

    product = IncompleteProduct("Телефон")

    with pytest.raises(AttributeError):
        repr(product)
