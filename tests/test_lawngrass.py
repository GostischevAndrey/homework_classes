import pytest
from tests.conftest import product_1


def test_lawn_grass(grass_1):
    assert grass_1.name == "Газонная трава"
    assert grass_1.description == "Элитная трава для газона"
    assert grass_1.price == 500.0
    assert grass_1.quantity == 20
    assert grass_1.country == "Россия"
    assert grass_1.germination_period == "7 дней"
    assert grass_1.color == "Зеленый"


def test_smartphone_error(grass_1):
    with pytest.raises(TypeError):
        grass_1 + product_1 # noqa


def test_smartphone_add(grass_1, grass_2):
    total_value = grass_1 + grass_2
    expected_value = (grass_1.price * grass_1.quantity) + (grass_2.price * grass_2.quantity)
    assert total_value == expected_value
