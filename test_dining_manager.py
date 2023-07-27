from dining_manager import calculate_total, display_menu, validate_quantity
import sys
from io import StringIO

def test_display_menu():
    expected_output = """Bienvenido(a) al Administrador de Experiencias Gastronómicas
Menú:
1. Pollo con almendras - $10.00 (Comida China)
2. Chow Mein - $8.00 (Comida China)
3. Arroz Frito - $7.00 (Comida China)
4. Wantan - $6.00 (Comida China)
5. Bentobox - $5.00 (Comida China)
6. Platillo Especial - $15.00 (Especialidades del Chef)\n
"""

    # Capture the output by redirecting stdout to a StringIO object
    captured_output = StringIO()
    sys.stdout = captured_output

    # Call the function that prints to stdout
    display_menu()

    # Reset stdout back to the original value
    sys.stdout = sys.__stdout__

    # Check if the expected output matches the actual output
    assert captured_output.getvalue() == expected_output


def test_calculate_total():
    # Test case with no order items (line 13)
    order_items = {}
    assert calculate_total(order_items) == -1

    # Test case with an invalid order item number (line 29)
    order_items = {"7": 2}  # Use a valid item number that is not in the menu
    assert calculate_total(order_items) == -1

    # Test case with a single item from the regular category (line 41)
    order_items = {"1": 2}
    assert calculate_total(order_items) == 20

    # Test case with a single item from the special category (5% surcharge) (lines 38, 39, 41)
    order_items = {"6": 1}
    assert calculate_total(order_items) == 15.75

    # Test case with a mix of regular and special category items (5% surcharge) (lines 38, 39, 41)
    order_items = {"1": 1, "6": 2}
    assert calculate_total(order_items) == 41.5

    # Test case with more than one quantity of each item (branch when len(order_items) >= 5) (line 47)
    order_items = {"1": 3, "6": 3}
    assert calculate_total(order_items) == 67.25

    # Test case with more than 5 items and total cost > 50 (branch when total_cost > 50) (line 53)
    order_items = {"1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
    assert calculate_total(order_items) == 32.4

    # Test case with more than 5 items and total cost > 100 (branch when total_cost > 100) (line 56)
    order_items = {"1": 2, "2": 2, "3": 2, "4": 2, "5": 2}
    assert calculate_total(order_items) == 54.8

    # Test case with more than 10 items (branch when len(order_items) >= 10) (line 49)
    order_items = {"1": 2, "2": 2, "3": 2, "4": 2, "5": 2, "6": 2, "7": 2, "8": 2, "9": 2, "10": 2}
    assert calculate_total(order_items) == 64.52

    # Test case with large quantities of items (branch when len(order_items) >= 10 and total_cost > 100) (line 50, 56)
    order_items = {"1": 20, "2": 20, "3": 20, "4": 20, "5": 20, "6": 20, "7": 20, "8": 20, "9": 20, "10": 20}
    assert calculate_total(order_items) == 710.2

    # Test case with an empty order_items dictionary (branch when len(order_items) == 0) (line 44)
    order_items = {}
    assert calculate_total(order_items) == -1

    # Test case with total_cost <= 0 (branch when total_cost <= 0) (line 44)
    order_items = {"1": -1}
    assert calculate_total(order_items) == -1

    # Test case with total_cost <= 50 (branch when total_cost > 50) (line 53)
    order_items = {"1": 6}
    assert calculate_total(order_items) == 50

    # Test case with total_cost > 50 (branch when total_cost > 50) (line 53)
    order_items = {"1": 7}
    assert calculate_total(order_items) == 60

    # Test case with total_cost > 100 (branch when total_cost > 100) (line 56)
    order_items = {"1": 13}
    assert calculate_total(order_items) == 95

    # Test case with total_cost <= 100 (branch when total_cost > 100) (line 56)
    order_items = {"1": 9}
    assert calculate_total(order_items) == 80

    # Test case with total_cost > 50 and total_cost > 100 (branch when total_cost > 50 and total_cost > 100) (line 53, 56)
    order_items = {"1": 8}
    assert calculate_total(order_items) == 70

    # Test case with total_cost <= 50 and total_cost > 100 (branch when total_cost > 50 and total_cost > 100) (line 53, 56)
    order_items = {"1": 12}
    assert calculate_total(order_items) == 85

    # Test case with total_cost > 50 and total_cost <= 100 (branch when total_cost > 50 and total_cost > 100) (line 53, 56)
    order_items = {"1": 5}
    assert calculate_total(order_items) == 50

    # Test case with total_cost <= 50 and total_cost <= 100 (branch when total_cost > 50 and total_cost > 100) (line 53, 56)
    order_items = {"1": 3}
    assert calculate_total(order_items) == 30

    # Test case with total_cost > 100 (branch when total_cost > 100)
    order_items = {"1": 11}
    assert calculate_total(order_items) == 100

    # Test case with total_cost > 50 and total_cost <= 100 (branch when total_cost > 50 and total_cost > 100) (line 58)
    order_items = {"1": 7}
    assert calculate_total(order_items) == 60

    # Test case with total_cost <= 50 and total_cost <= 100 (branch when total_cost > 50 and total_cost > 100) (line 58)
    order_items = {"1": 4}
    assert calculate_total(order_items) == 40
    from dining_manager import validate_quantity

def test_validate_quantity():
    # Test case with a valid quantity
    assert validate_quantity("10") == 10

    # Test case with a quantity of 0 (should return -1)
    assert validate_quantity("0") == -1

    # Test case with a negative quantity (should return -1)
    assert validate_quantity("-5") == -1

    # Test case with a quantity greater than 100 (should return -1)
    assert validate_quantity("200") == -1

    # Test case with a non-integer quantity (should return -1)
    assert validate_quantity("abc") == -1


