MetroMind: Shortest-Route and Fare Computation Engine

Team

- Gayathri KM (1AT24IS061)
- Jeevitha KM (1AT24IS077)

Project: MetroMind
Technology: Python
Algorithm: Breadth-First Search (BFS)

How to Run

1. Install Python 3 on your system.
2. Download or clone the MetroMind repository.
3. Open the project folder in VS Code or a terminal.
4. Run the following command:

python main.py

5. Enter the starting station, destination station, and travel card balance when prompted.

Features That Work

1. Metro Network Representation: Stores metro stations and their direct connections using a Python dictionary.
2. Shortest Route Finding: Uses the BFS algorithm to find the route with the minimum number of stops in an unweighted graph.
3. Station Validation: Checks whether the entered starting and destination stations exist.
4. Interchange Detection: Identifies interchange stations along the selected route.
5. Fare Calculation: Calculates fares based on the number of stops using predefined fare slabs.
6. Travel Card Balance: Accepts the user's card balance and checks whether it is sufficient.
7. Fare Deduction: Deducts the fare when sufficient balance is available and displays the remaining balance.
8. Input Handling: Handles invalid station names and invalid balance inputs.

Sample Run

Welcome to MetroMind!

Enter station name: Airport
Enter destination station: Tech Park

Shortest Route:
Airport -> Terminal -> City -> Majestic
-> Central Square -> Stadium -> Market -> Tech Park

Total Stops: 7

Interchange Stations:
Majestic, Central Square

Total Fare: Rs. 40

Enter travel card balance: 100

Payment successful.
Fare deducted: Rs. 40
Remaining balance: Rs. 60

Journey Confirmed!

Note: The metro network and fare structure are illustrative and created for this project.