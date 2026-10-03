import pytest
from praktikum.burger import Burger
from unittest.mock import Mock
from typing import List

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100
    return bun

@pytest.fixture
def mock_ingredient_sauce():
    ingredient = Mock()
    ingredient.get_type.return_value = 'SAUCE'
    ingredient.get_name.return_value = "hot sauce"
    ingredient.get_price.return_value = 100
    return ingredient

@pytest.fixture
def mock_ingredient_filling():
    ingredient = Mock()
    ingredient.get_type.return_value = 'FILLING'
    ingredient.get_name.return_value = "cutlet"
    ingredient.get_price.return_value = 100
    return ingredient

@pytest.fixture
def burger_two_ingredients_filling_sauce_bun(burger, mock_bun, mock_ingredient_filling, mock_ingredient_sauce):
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_filling)
    burger.add_ingredient(mock_ingredient_sauce)
    return burger        
