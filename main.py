from metro_data import metro, metro_lines
from route_finder import bfs, validate_station, find_interchanges
from fare_manager import calculate_fare, get_balance, deduct_fare


def main():
    print("\n====================================")
    print("Welcome to MetroMind!")
    print("====================================")

    start = input("Enter station name: ").strip().title()
    destination = input("Enter destination station: ").strip().title()

    # Validate starting station
    if not validate_station(metro, start):
        print("Invalid start station. Please enter a valid station name.")
        return

    # Validate destination station
    if not validate_station(metro, destination):
        print("Invalid destination station. Please enter a valid station name.")
        return

    # Find shortest route
    route = bfs(metro, start, destination)

    if route is None:
        print(f"No route found from {start} to {destination}.")
        return

    # Display journey details
    print("\n========== JOURNEY DETAILS ==========")

    print("Shortest route:", " -> ".join(route))
    print("Number of stations:", len(route))
    print("Number of stops:", len(route) - 1)

    # Identify interchange stations
    interchanges = find_interchanges(route, metro_lines)

    if interchanges:
        print("Interchange stations:", ", ".join(interchanges))
    else:
        print("Interchange stations: None")

    print("Number of interchanges:", len(interchanges))

    # Calculate fare
    fare = calculate_fare(route)

    print("\n========== FARE DETAILS ==========")
    print("Total fare: ₹", fare)

    # Travel card payment
    print("\n========== TRAVEL CARD ==========")

    balance = get_balance()
    balance, payment_status = deduct_fare(balance, fare)

    # Display journey summary
    print("\n========== JOURNEY SUMMARY ==========")

    print("From:", start)
    print("To:", destination)
    print("Calculated fare: ₹", fare)

    if fare == 0:
        print("No fare required.")
        print("Journey status: Confirmed")

    elif payment_status:
        print("Payment status: Successful")
        print("Journey status: Confirmed")

    else:
        print("Payment status: Failed")
        print("Journey status: Not confirmed")

    print("Final card balance: ₹", balance)


if __name__ == "__main__":
    main()
