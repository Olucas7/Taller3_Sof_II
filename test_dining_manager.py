# test_dining_manager.py

from dining_manager import calculate_total

# Menú con ingredientes ecuatorianos y sus precios
menu = {
    "1": {"name": "Humita", "price": 6},
    "2": {"name": "Bolon de Verde", "price": 5},
    "3": {"name": "Tigrillo", "price": 8},
}

# Casos de prueba para la función calculate_total

def test_calculate_total_sin_items():
    # Prueba con order_items vacío
    assert calculate_total({}) == 0

def test_calculate_total_un_item():
    # Prueba con un solo platillo
    order_items_1 = {"1": 2}  # 2 Humitas
    assert calculate_total(order_items_1) == 6 * 2  # El precio de una humita es 6, por lo tanto, el total debe ser 6 * 2 = 12

def test_calculate_total_varios_items():
    # Prueba con varios platillos
    order_items_2 = {"1": 2, "2": 1, "3": 3}  # 2 Humitas, 1 Bolon de Verde, 3 Tigrillos
    assert calculate_total(order_items_2) == 6*2 + 5*1 + 8*3  # El total debe ser la suma de los precios de los platillos seleccionados

def test_calculate_total_item_invalido():
    # Prueba con un número de platillo inválido (no está en el menú)
    order_items_3 = {"4": 1}  # Número de platillo inválido
    assert calculate_total(order_items_3) == 0  # Dado que el platillo no está en el menú, el costo total debe ser 0

def test_calculate_total_cantidad_negativa():
    # Prueba con cantidad negativa para un platillo
    order_items_4 = {"1": -2}  # Cantidad negativa para Humita
    assert calculate_total(order_items_4) == 0  # Dado que la cantidad es negativa, el costo total debe ser 0

if __name__ == "__main__":
    pytest.main()
