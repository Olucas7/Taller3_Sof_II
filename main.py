from dining_manager import *

def main():
    display_menu()

    order_items = {}
    while True:
        item = input("Ingrese el número del platillo que desea ordenar (presione Enter para finalizar): ")
        if not item:
            break

        quantity = input("Ingrese la cantidad: ")
        quantity = validate_quantity(quantity)
        if quantity == -1:
            print("Cantidad inválida. Por favor, ingrese una cantidad válida (entero positivo entre 1 y 100).")
            continue

        if item in menu:
            order_items[item] = order_items.get(item, 0) + quantity
        else:
            print("Número de platillo inválido. Por favor, inténtelo nuevamente.")

    total_cost = calculate_total(order_items)
    if total_cost == -1:
        print("Orden cancelada debido a datos inválidos.")
    else:
        print("Resumen de la orden:")
        for item, quantity in order_items.items():
            print(f"{menu[item]['name']} - Cantidad: {quantity}")
        print(f"Total de la orden: ${total_cost}")

if __name__ == "__main__":
    main()
