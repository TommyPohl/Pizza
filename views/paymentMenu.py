from models.payment import Payment

def show_payment_menu(amount):
    print("\n=== PLATBA ===")
    print(f"Celková částka k zaplacení: {amount:.2f} Kč")
    print("Zvolte způsob platby:")
    print("1. Hotově")
    print("2. Kartou")
    print("3. Online převod")
    print("0. Zpět")

    choice = input("Vaše volba: ")

    if choice == "1":
        method = "cash"
    elif choice == "2":
        method = "card"
    elif choice == "3":
        method = "online"
    elif choice == "0":
        print("Vracíme se zpět...")
        return None
    else:
        print("Neplatná volba. Zkuste to znovu.")
        return show_payment_menu(amount)

    payment = Payment(amount, method)

    try:
        success = payment.process_payment()
        if success:
            print("Platba proběhla úspěšně.")
            return payment
    except ValueError as e:
        print(f"Chyba při platbě: {e}")

    return None
