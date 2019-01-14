from pprint import pprint


def read_sorted_input(filename):
    input = open(filename, 'r').read().split('\n')
    sorted_input = sorted(input)
    return sorted_input


def scan_line(line):
    line = line.split(" ")
    action = line[2]
    return {
        'minute': int(line[1].split(":")[1][:-1]),
        'action': action,
        'guard_id': int(line[3][1:]) if action == 'Guard' else None,
    }


def analyze_registry(registry):
    schedule = create_schedule()
    state = 'init'
    current_guard_id = None
    falls_at = None
    wakes_at = None

    for line in registry:
        line = scan_line(line)

        # State init
        if state == 'init':
            if line['action'] == 'Guard':
                current_guard_id = line['guard_id']
                state = 'A'
            continue

        # State A (guard starts shift)
        if state == 'A':
            if line['action'] == 'falls':
                falls_at = line['minute']
                state = 'B'
            continue

        # State B (guard falls asleep)
        if state == 'B':
            if line['action'] == 'wakes':
                wakes_at = line['minute']
                state = 'C'
            continue

        # State C (wakes up)
        if state == 'C':
            # Update schedule
            schedule = update_schedule(schedule, current_guard_id, falls_at, wakes_at)
            if line['action'] == 'falls':
                falls_at = line['minute']
                state = 'B'
            if line['action'] == 'Guard':
                current_guard_id = line['guard_id']
                state = 'A'
            continue

    return schedule


def update_schedule(schedule, guard_id, init, end):
    if guard_id not in schedule:
        schedule[guard_id] = [0 for n in range(60)]
    for n in range(init, end):
        schedule[guard_id][n] += 1
    return schedule


def create_schedule():
    return {}


def schedule_winner(schedule):
    return max([(x[0], sum(x[1])) for x in schedule.items()],
               key=lambda x: x[1])[0]


if __name__ == '__main__':
    input = read_sorted_input('input.txt')[1:]

    schedule = analyze_registry(input)
    winner = schedule_winner(schedule)
    winner_minute = schedule[winner].index(max(schedule[winner]))
    print(winner * winner_minute)


"""
{99: [0, 0, 0, 0, 0...], -> 2
 10: [1, 0, 1, 0, 0...]} -> 4
"""
