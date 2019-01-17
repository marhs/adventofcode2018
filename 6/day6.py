def print_canvas(canvas):
    for row in canvas:
        print(''.join([' ' + str(x) + ' ' for x in row]))


def generate_canvas(x, y, input):
    canvas = [['.' for _ in range(x)] for _ in range(y)]
    for x, y, c in input:
        canvas[y][x] = str(c)
    return canvas


def input_to_coords(input, offset=0):
    """
    (x, y, id)
    """
    lines = input.split('\n')
    res = []
    counter = 0
    for line in lines:
        x, y = line.split(', ')
        res.append((int(x)+offset, int(y)+offset, str(counter)))
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


# Part b

def calculate_distances(canvas, initial_points):
    for y in range(len(canvas)):
        for x in range(len(canvas[y])):
            distance = total_distance(x, y, initial_points)
            canvas[y][x] = distance
    return canvas


def total_distance(x, y, initial_points):
    res = {}
    for point in initial_points:
        res[point[2]] = manhattan_distance(x, y, point[0], point[1])
    distances = sum(res.values())
    return distances


def count_region(canvas):
    region_size = 0
    for row in canvas:
        for elem in row:
            if elem < 10000:
                region_size += 1
    return region_size


if __name__ == '__main__':
    filename = 'input.txt'
    input = open(filename, 'r').read()[:-1]
    points = input_to_coords(input, offset=300)
    canvas = generate_canvas(800, 800, points)

    # Part a
    # canvas, areas = search_points(canvas, points)
    # infinite_areas = detect_infinite_areas(canvas)
    # print(solution(areas, infinite_areas))

    # Part b
    canvas = calculate_distances(canvas, points)
    print(count_region(canvas))


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
