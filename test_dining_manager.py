import pytest
from dining_manager import validate_quantity, calculate_total

def test_validate_quantity():
    assert validate_quantity(0) == -1
    assert validate_quantity(-5) == -1
    assert validate_quantity(101) == -1
    assert validate_quantity(3) == 3
    assert validate_quantity(100) == 100

def test_calculate_total():
    # Test with empty order_items
    assert calculate_total({}) == -1

    # Test with one item
    order_items_1 = {"1": 2}  # 2 Pollo con almendras
    assert calculate_total(order_items_1) == 10 * 2

    # Test with multiple items
    order_items_2 = {"1": 2, "2": 1, "3": 3}  # 2 Pollo con almendras, 1 Chow Mein, 3 Arroz Frito
    assert calculate_total(order_items_2) == 10 * 2 + 8 * 1 + 7 * 3

    # Test with special category
    order_items_3 = {"1": 1, "3": 1}  # 1 Pollo con almendras, 1 Arroz Frito (ambos de categoría especial)
    assert calculate_total(order_items_3) == int((10 + 10 * 0.05) + (7 + 7 * 0.05))

    # Test with discount for more than 5 items
    order_items_4 = {"1": 1, "2": 1, "3": 1, "4": 1, "5": 1}  # 5 platillos diferentes
    assert calculate_total(order_items_4) == int(36 * 0.9)
