from models.pizza import Pizza
from models.topping import Topping


def show_order_menu():
    print("\n=== OBJEDNÁVKA PIZZY ===")

    pizza = choose_pizza()

    while True:
        print("\nAktuální pizza:", pizza)
        print("1. Přidat přílohu")
        print("2. Dokončit objednávku")
        print("3. Zrušit objednávku")
        choice = input("Zadejte volbu: ")

        if choice == "1":
            topping = choose_topping()
            if topping:
                pizza.add_topping(topping)
        elif choice == "2":
            print("\nObjednávka dokončena:")
            print(pizza)
            return pizza
        elif choice == "3":
            print("Objednávka zrušena.")
            return None
        else:
            print("Neplatná volba. Zkuste znovu.")


def choose_pizza():
    print("\nVyberte typ pizzy:")
    print("1. Margherita (120 Kč)")
    print("2. Salami (135 Kč)")
    print("3. Quattro Formaggi (150 Kč)")

    choice = input("Zadejte volbu: ")

    if choice == "1":
        return Pizza("Margherita", 120)
    elif choice == "2":
        return Pizza("Salami", 135)
    elif choice == "3":
        return Pizza("Quattro Formaggi", 150)
    else:
        print("Neplatná volba, výběr opakuji.")
        return choose_pizza()


def choose_topping():
    print("\nDostupné přílohy:")
    print("1. Sýr navíc (+20 Kč)")
    print("2. Šunka (+25 Kč)")
    print("3. Feferonky (+15 Kč)")
    print("0. Zpět")

    choice = input("Zadejte volbu: ")

    if choice == "1":
        return Topping("Sýr navíc", 20)
    elif choice == "2":
        return Topping("Šunka", 25)
    elif choice == "3":
        return Topping("Feferonky", 15)
    elif choice == "0":
        return None
    else:
        print("Neplatná volba.")
        return choose_topping()
