import pytest
from praktikum.burger import Burger
from unittest.mock import Mock


class TestBurger:

    def test_set_bun(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        
        assert burger.bun.get_name() == "black bun"

    def test_add_ingredient_filling(self, burger, mock_ingredient_filling):
        burger.add_ingredient(mock_ingredient_filling)

        assert burger.ingredients[0].get_name() == "cutlet"

    def test_add_ingredient_filling_and_sauce(self, burger, mock_ingredient_filling, mock_ingredient_sauce):
        burger.add_ingredient(mock_ingredient_filling)
        burger.add_ingredient(mock_ingredient_sauce)

        assert len(burger.ingredients) == 2
        
    def test_remove_ingredient_one(self, burger_two_ingredients_filling_sauce_bun):
        burger_two_ingredients_filling_sauce_bun.remove_ingredient(0)
        burger_one_ingredients = burger_two_ingredients_filling_sauce_bun

        assert len(burger_one_ingredients.ingredients) == 1

    def test_move_ingredient_filling(self, burger_two_ingredients_filling_sauce_bun):
        burger_two_ingredients_filling_sauce_bun.move_ingredient(0, 1)

        burger_two_ingredients_sauce_filling = burger_two_ingredients_filling_sauce_bun
        
        assert burger_two_ingredients_sauce_filling.ingredients[0].get_type() == "SAUCE"

    @pytest.mark.parametrize(
        "bun_price, ing_prices, expected_total",
        [
            # Бургер: Булка 100, котлета 100
            (100.0, [100.0], 300.0),
            
            # Бургер: Булка 70. Сумма: 70 * 2 = 140
            (70.0, [], 140.0),
            
            # Бургер: Булка 80, котлета 100, соус 50
            (80.0, [100.0, 50.0], 310.0),
            
            # Бургер: Булка 99.90, соус 0.0, Сумма: 99.90 * 2 = 199.80
            (99.90, [0.0], 199.80)
        ]
    )
    def test_calculate_burger_price(self, burger, mock_bun, bun_price, ing_prices, expected_total):
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)
        
        for price in ing_prices:
            mock_ingredient = Mock()
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)
            
        assert burger.get_price() == expected_total
    
    def test_get_receipt_two_ingridients(self, burger_two_ingredients_filling_sauce_bun):

        receipt = burger_two_ingredients_filling_sauce_bun.get_receipt()
        
        assert receipt == "(==== black bun ====)\n= filling cutlet =\n= sauce hot sauce =\n(==== black bun ====)\n\nPrice: 400"