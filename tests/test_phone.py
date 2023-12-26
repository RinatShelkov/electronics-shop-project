import pytest

from src.phone import Phone


@pytest.fixture
def phone_1():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    return phone1


def test_phone(phone_1):
    assert repr(phone_1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone_1.number_of_sim == 2
    phone_1.number_of_sim = 50


def test_invalid_simcard(phone_1):
    with pytest.raises(ValueError):
        phone_1.number_of_sim = 0
