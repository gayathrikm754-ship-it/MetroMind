# MetroMind: Shortest-Route and Fare Computation Engine

## 1\. Project Overview

MetroMind is a Python-based, console application designed to find the shortest route between two metro stations and calculate the corresponding travel fare.

The application uses a fictional metro network consisting of three lines: Blue Line, Green Line and Orange Line.

It helps passengers:

- Find the shortest route between two stations.
- Identify interchange stations.
- Calculate journey fares.
- Check travel card balance.
- Deduct fares when sufficient balance is available.

## 2\. Problem Statement

Navigating a metro network involves identifying suitable routes, understanding interchange points and calculating travel costs.

MetroMind addresses this problem using graph representation and the Breadth-First Search (BFS) algorithm to find routes with the minimum number of stops.

## 3\. Technologies Used

| Technology | Purpose |
| --- | --- |
| Python | Core programming language |
| BFS | Shortest-route calculation |
| Dictionaries | Store stations and connections |
| Lists | Store neighbouring stations and metro lines |
| Sets | Track visited stations |
| Deque | Implement the BFS queue |
| Decimal | Fare and balance calculations |

## 4\. Features

1. Stores metro stations and their direct connections.
2. Supports three fictional metro lines: Blue, Green and Orange.
3. Finds the shortest route using BFS.
4. Displays the complete route and number of stops.
5. Identifies interchange stations.
6. Calculates fares based on the number of stops.
7. Accepts and validates travel card balance.
8. Deducts fare when sufficient balance is available.
9. Handles insufficient balance and invalid station inputs.
10. Supports journeys where the starting station and destination are the same.

## 5\. Project Structure

``` text
MetroMind/
│
├── main.py
├── metro_data.py
├── route_finder.py
├── fare_manager.py
├── README.md
└── .gitignore
```

### File Description

- **main.py:** Handles program execution and user interaction.
- **metro\_data.py:** Stores metro stations, connections and line information.
- **route\_finder.py:** Implements BFS, station validation and interchange detection.
- **fare\_manager.py:** Handles fare calculation, balance validation and payment.

## 6\. Algorithm Used

### Breadth-First Search (BFS)

MetroMind uses the Breadth-First Search algorithm to find the route with the minimum number of stops between two stations.

The metro network is represented as an unweighted graph.

BFS explores neighbouring stations level by level using a queue.

The implementation uses:

- **Queue:** Stores stations waiting to be explored.
- **Visited Set:** Prevents repeated visits to stations.
- **Parent Dictionary:** Stores the previous station to reconstruct the shortest route.

After reaching the destination, the parent dictionary is used to reconstruct the complete route.

## 7\. Fare Calculation

The fare is calculated based on the number of stops.

| Number of Stops | Fare |
| --- | ---: |
| 0 | ₹0 |
| 1–2 | ₹10 |
| 3–4 | ₹20 |
| 5–6 | ₹30 |
| More than 6 | ₹40 |

*Note: These are illustrative fare rules defined for this project.*

## 8\. How to Run the Application

### Prerequisites

- Python 3 installed on your system.
- A code editor or terminal.

### Execution Steps

1. Clone or download the project repository.
2. Open the MetroMind folder in a terminal.
3. Run the following command:

``` bash
python main.py
```

4. Enter the starting station.
5. Enter the destination station.
6. Enter your travel card balance.
7. View the shortest route, interchange details, fare and journey summary.

## 9\. Limitations

- Uses a fictional metro network with predefined station connections.
- Calculates routes based on the minimum number of stops, not actual travel time.
- Uses illustrative fare slabs rather than actual metro fares.
- Travel card balance is entered manually and is not permanently stored.
- Runs as a console-based application.

## 10\. Future Enhancements

- Add more metro stations and lines.
- Introduce travel-time-based route calculation.
- Support persistent travel card balances.
- Implement off-peak fare discounts.
- Provide nearby station suggestions.

## 11\. Conclusion

MetroMind demonstrates the application of graph representation and the Breadth-First Search algorithm to a metro route-finding problem.

By combining shortest-route calculation, interchange detection and fare management, the project provides a simple console-based metro journey planning system.

## 12\. Team Members

| Name | Role |
| --- | --- |
| Gayathri KM | Developer |
| Jeevitha KM | Developer |