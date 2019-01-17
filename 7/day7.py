from bisect import insort

test_restrictions = {
    'A': set(['C']),
    'B': set(['A']),
    'C': set([]),
    'D': set(['A']),
    'E': set(['B', 'D', 'F']),
    'F': set(['C'])
}


def kahns_algorithm(restrictions):
    final_order = []
    free_steps = sorted(
        [node for node, rest in restrictions.items() if len(rest) == 0]
    )
    while len(free_steps) > 0:
        step = free_steps[0]
        free_steps = free_steps[1:]
        del restrictions[step]
        final_order.append(step)
        for key in restrictions.keys():
            if step in restrictions[key]:
                restrictions[key].remove(step)
                if len(restrictions[key]) == 0:
                    insort(free_steps, key)

    return ''.join(final_order)


def parse_input(input):
    restrictions = {}

    for line in input:
        words = line.split()
        node_a = words[1]
        node_b = words[7]

        # Update nodes
        if node_a not in restrictions:
            restrictions[node_a] = set()
        if node_b not in restrictions:
            restrictions[node_b] = set()

        # Update restrictions
        restrictions[node_b].add(node_a)

    return restrictions


if __name__ == "__main__":
    filename = 'input.txt'
    input = open(filename, 'r').read()[:-1].split('\n')

    # Parse input
    restrictions = parse_input(input)

    # Kahns
    print(kahns_algorithm(restrictions))

"""
nodes = ['A', 'B', 'C', 'D', 'E', 'F']
restrictions = {
    'A': set(['C']),
    'B': set(['A']),
    'C': set([]),
    'D': set(['A']),
    'E': set(['B', 'D', 'F']),
    'F': set(['C'])
}
"""
