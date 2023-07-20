import unittest
from dining_manager import validate_quantity, calculate_total

class TestDiningManager(unittest.TestCase):

    def test_validate_quantity(self):
        self.assertEqual(validate_quantity(0), -1)
        self.assertEqual(validate_quantity(-5), -1)
        self.assertEqual(validate_quantity(101), -1)
        self.assertEqual(validate_quantity(3), 3)
        self.assertEqual(validate_quantity(100), 100)

    def test_calculate_total(self):
        # Test with empty order_items
        self.assertEqual(calculate_total({}), -1)

        # Test with one item
        order_items_1 = {"1": 2}  # 2 Pollo con almendras
        self.assertEqual(calculate_total(order_items_1), 10 * 2)

        # Test with multiple items
        order_items_2 = {"1": 2, "2": 1, "3": 3}  # 2 Pollo con almendras, 1 Chow Mein, 3 Arroz Frito
        self.assertEqual(calculate_total(order_items_2), 10 * 2 + 8 * 1 + 7 * 3)

        # Test with special category
        order_items_3 = {"1": 1, "3": 1}  # 1 Pollo con almendras, 1 Arroz Frito (ambos de categoría especial)
        self.assertEqual(calculate_total(order_items_3), int((10 + 10 * 0.05) + (7 + 7 * 0.05)))

        # Test with discount for more than 5 items
        order_items_4 = {"1": 1, "2": 1, "3": 1, "4": 1, "5": 1}  # 5 platillos diferentes
        expected_total_cost = int(36 * 0.9)
        self.assertEqual(calculate_total(order_items_4), expected_total_cost)
