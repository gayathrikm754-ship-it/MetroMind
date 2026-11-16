from collections import deque


def bfs(metro, start, destination):
    queue = deque([start])
    visited = {start}
    parent = {start: None}

    while queue:
        node = queue.popleft()

        if node == destination:
            break

        for neighbour in metro[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                parent[neighbour] = node
                queue.append(neighbour)

    # Check whether destination is reachable
    if destination not in parent:
        return None

    # Reconstruct the shortest path
    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path


def validate_station(metro, station):
    return station in metro


def find_interchanges(route, metro_lines):
    interchange_stations = []

    for station in route:
        if station in metro_lines:
            if len(metro_lines[station]) > 1:
                interchange_stations.append(station)

    return interchange_stations
