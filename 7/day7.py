from bisect import insort
from string import ascii_uppercase

test_restrictions = {
    'A': set(['C']),
    'B': set(['A']),
    'C': set([]),
    'D': set(['A']),
    'E': set(['B', 'D', 'F']),
    'F': set(['C'])
}

task_order = 'CABDFE'


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


# Part A
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

    return final_order


def task_duration(task_name, offset=60):
    return ascii_uppercase.index(task_name) + offset + 1


def task_finished(task_name, task_restrictions):
    for key in task_restrictions:
        if task_name in task_restrictions[key]:
            task_restrictions[key].remove(task_name)
    return task_restrictions


def workload_distributor(task_order, task_restrictions, num_workers):
    done_tasks = []
    busy_workers = {}  # set([['A', 9], ['B', 1]])
    time = 0
    total_tasks = len(task_restrictions)
    while (len(done_tasks) != total_tasks):
        # Update current busy workers
        tasks_in_progress = list(busy_workers.keys())
        for task_name in tasks_in_progress:
            # Update elapsed time
            elapsed_time = busy_workers[task_name]
            busy_workers[task_name] += 1
            # Check finished tasks
            if task_duration(task_name) == elapsed_time+1:
                del busy_workers[task_name]
                task_restrictions = task_finished(task_name, task_restrictions)
                done_tasks.append(task_name)

        # Assign new tasks
        task_to_do = [
            task
            for task, restrictions
            in task_restrictions.items()
            if len(restrictions) == 0
        ]

        for task in task_to_do:
            if ((num_workers - len(busy_workers)) > 0 and
                    len(task_restrictions[task]) == 0):
                busy_workers[task] = 0
                del task_restrictions[task]
            else:
                break

        # Update time
        time += 1

    return time - 1


if __name__ == "__main__":
    filename = 'input.txt'
    input = open(filename, 'r').read()[:-1].split('\n')

    # Parse input
    restrictions = parse_input(input)

    # Kahns - Part A
    task_order = kahns_algorithm(restrictions)

    restrictions = parse_input(input)
    # Workload - Part B
    print(workload_distributor(task_order, restrictions, 5))


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
