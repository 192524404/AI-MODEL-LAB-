
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': ['I']
}

heuristic = {
    'A': 5, 'B': 2, 'C': 1, 'D': 4,
    'E': 3, 'F': 5, 'G': 0, 'H': 4, 'I': 6
}

def beam_search(start, goal, width):
    beam = [[start]]

    while beam:
        candidates = []

        for path in beam:
            node = path[-1]

            if node == goal:
                return path

            for child in graph.get(node, []):
                candidates.append(path + [child])

        candidates.sort(key=lambda p: heuristic[p[-1]])
        beam = candidates[:width]

    return None


start = 'A'
goal = 'G'
width = 2

path = beam_search(start, goal, width)

if path:
    print("Best Path:", " -> ".join(path))
else:
    print("Goal not found")
