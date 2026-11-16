from decimal import Decimal, InvalidOperation


def calculate_fare(route):
    stops = len(route) - 1

    if stops == 0:
        fare = Decimal("0")
    elif stops <= 2:
        fare = Decimal("10")
    elif stops <= 4:
        fare = Decimal("20")
    elif stops <= 6:
        fare = Decimal("30")
    else:
        fare = Decimal("40")

    return fare


def get_balance():
    while True:
        try:
            balance = Decimal(input("Enter travel card balance: ").strip())

            if not balance.is_finite():
                print("Please enter a valid number.")
                continue

            if balance < 0:
                print("Balance cannot be negative.")
                continue

            return balance

        except InvalidOperation:
            print("Invalid input. Please enter a valid number.")


def deduct_fare(balance, fare):
    if balance >= fare:
        balance -= fare

        print("Payment successful.")
        print("Fare deducted: ₹", fare)
        print("Remaining balance: ₹", balance)

        return balance, True

    else:
        print("Insufficient balance. Please recharge your travel card.")
        return balance, False
