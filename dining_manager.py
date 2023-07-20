
# Menú con ingredientes ecuatorianos y sus precios
menu = {
    "1": {"name": "Humita", "price": 6},
    "2": {"name": "Bolon de Verde", "price": 5},
    "3": {"name": "Tigrillo", "price": 8},
}

def display_menu():
    print("Bienvenido(a) al Administrador de Comidas")
    print("Menú:")
    for key, item in menu.items():
        print(f"{key}. {item['name']} - ${item['price']:.2f}")
    print()

def calculate_total(order_items):
    total_cost = 0
    for item, quantity in order_items.items():
        if item in menu and quantity > 0:
            total_cost += menu[item]['price'] * quantity
    return total_cost

def main():
    display_menu()

    order_items = {}
    while True:
        item = input("Ingrese el número del platillo que desea ordenar (presione Enter para finalizar): ")
        if not item:
            break

        quantity = int(input("Ingrese la cantidad: "))
        if item in menu:
            order_items[item] = order_items.get(item, 0) + quantity
        else:
            print("Número de platillo inválido. Por favor, inténtelo nuevamente.")

    total_cost = calculate_total(order_items)
    print(f"Total de su orden: ${total_cost:.2f}")

if __name__ == "__main__":
    main()