def print_canvas(canvas):
    for row in canvas:
        print(''.join(row))


def generate_canvas(x, y, input):
    canvas = [['.' for _ in range(x)] for _ in range(y)]
    for x, y, c in input:
        canvas[y][x] = str(c)
    return canvas


def input_to_coords(input):
    """
    (x, y, id)
    """
    lines = input.split('\n')
    res = []
    counter = 0
    for line in lines:
        x, y = line.split(', ')
        res.append((int(x), int(y), str(counter)))
        counter += 1
    return res


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def nearest_point(x, y, initial_points):
    res = {}
    for point in initial_points:
        res[point[2]] = manhattan_distance(x, y, point[0], point[1])

    distances = sorted(res.values())
    if distances[0] == distances[1]:
        return '*'
    else:
        return min(res.items(), key=lambda x: x[1])[0]


def search_points(canvas, initial_points):
    """
    * : empate
    a : perteneciente a A
    . : no explorado
    """
    total_areas = {k[2]: 0 for k in initial_points}
    total_areas['*'] = 0
    for y in range(len(canvas)):
        for x in range(len(canvas[y])):
            point_id = nearest_point(x, y, initial_points)
            canvas[y][x] = point_id
            total_areas[point_id] += 1
    return canvas, total_areas


def detect_infinite_areas(canvas):
    areas = set()

    areas.update(set(canvas[0]))
    areas.update(set(canvas[len(canvas)-1]))
    for row in canvas:
        areas.add(row[0])
        areas.add(row[len(row)-1])

    return areas


def solution(areas, infinite_areas):
    res = {k: v for k, v in areas.items() if k not in infinite_areas}
    return max(res.values())


def generate_neighbours(x, y, x_lim=10, y_lim=10):
    res = []
    if (x + 1) < x_lim:
        res.append((x + 1, y))
    if (x - 1) >= 0:
        res.append((x - 1, y))
    if (y + 1) < y_lim:
        res.append((x, y + 1))
    if (y - 1) >= 0:
        res.append((x, y - 1))
    return res


if __name__ == '__main__':
    filename = 'input.txt'
    input = open(filename, 'r').read()[:-1]
    points = input_to_coords(input)
    canvas = generate_canvas(1000, 1000, points)
    canvas, areas = search_points(canvas, points)
    infinite_areas = detect_infinite_areas(canvas)
    print(solution(areas, infinite_areas))


"""
...................................................
.b.a...............................................
bBxAa.................................aAa..........
.b.a...................................a...........
...................................................
.......................................b...........
......................................bBb..........
...................................................
...................................................
...................................................
...................................................
.....................A.............................
...................................................
............................C......................
.......................D...........................
.........................E.........................
.....................B.....G.......................
.......................F...........................
...................................................
...................................................
...................................................
...................................................
...............x...................................
...............................x...................
...................................................
............................x......................
.............x............................r........
.......x................x..........................
...................................................
...................................................
"""
