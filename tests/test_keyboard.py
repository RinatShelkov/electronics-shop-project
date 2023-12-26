# -*- coding: utf-8 -*-
import pytest

from src.keyboard import Keyboard


@pytest.fixture
def kb():
    kb = Keyboard("Dark Project KD87A", 9600, 5)
    return kb


def test_keyboard(kb):
    assert str(kb) == "Dark Project KD87A"

    assert str(kb.language) == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"

    # Сделали EN -> RU -> EN
    kb.change_lang()
    assert str(kb.language) == "EN"
