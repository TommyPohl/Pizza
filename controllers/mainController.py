from views.paymentMenu import show_payment_menu
from views.orderMenu import show_order_menu

def finalize_order(total_amount):
    payment = show_payment_menu(total_amount)
    if payment and payment.is_paid():
        print("Objednávka byla úspěšně dokončena.")
    else:
        print("Platba se nezdařila nebo byla zrušena.")


def main_flow():
    pizza = show_order_menu()
    if pizza:
        total = pizza.get_total_price()
        show_payment_menu(total)