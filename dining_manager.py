# Menú con comidas y sus precios (se le asigna el tema "Comida China" para ejemplo)
menu = {
    "1": {"name": "Pollo con almendras", "price": 10, "category": "Comida China"},
    "2": {"name": "Chow Mein", "price": 8, "category": "Comida China"},
    "3": {"name": "Arroz Frito", "price": 7, "category": "Comida China"},
    "4": {"name": "Wantan", "price": 6, "category": "Comida China"},
    "5": {"name": "Bentobox", "price": 5, "category": "Comida China"},
    "6": {"name": "Platillo Especial", "price": 15, "category": "Especialidades del Chef"}
}

# Categoría de platillo especial con precio más alto (se le asigna el tema "Especialidades del Chef" para ejemplo)
special_category = "Especialidades del Chef"
special_category_surcharge = 0.05  # 5% de recargo para platillos de la categoría especial

def display_menu():
    print("Bienvenido(a) al Administrador de Experiencias Gastronómicas")
    print("Menú:")
    for key, item in menu.items():
        print(f"{key}. {item['name']} - ${item['price']:.2f} ({item['category']})")
    print()

def validate_quantity(quantity):
    try:
        quantity = int(quantity)
        if quantity <= 0 or quantity > 100:
            raise ValueError
        return quantity
    except ValueError:
        return -1

def calculate_total(order_items):
    total_cost = 0
    special_category_items = 0

    for item, quantity in order_items.items():
        if item in menu:
            meal_price = menu[item]['price']
            if menu[item]['category'] == special_category:
                special_category_items += quantity
                meal_price += meal_price * special_category_surcharge
            total_cost += meal_price * quantity

    if len(order_items) == 0 or total_cost <= 0:
        return -1

    if len(order_items) >= 5:
        total_cost *= 0.9

    if len(order_items) >= 10:
        total_cost *= 0.8

    if total_cost > 50:
        total_cost -= 10

    if total_cost > 100:
        total_cost -= 25

    return round(total_cost, 2)