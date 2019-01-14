input = open('input.txt', 'r').read()


def transform_claim(claim):
    """
    #1300 @ 339,57: 22x20
    {'id': 1300, 'x': 339, 'y', 57, 'w': 22, 'h': 20}
    """
    res = {}
    elements = claim.split()
    res['id'] = elements[0]
    res['x'], res['y'] = [int(x) for x in elements[2][:-1].split(',')]
    res['w'], res['h'] = [int(x) for x in elements[3].split('x')]
    return res


def update_fabric_claims(fabric_claims, claim):
    x, y = claim['x'], claim['y']
    w, h = claim['w'], claim['h']
    for i in range(h):
        for j in range(w):
            fabric_claims[y+i][x+j] += 1
    return fabric_claims


def count_overlap(fabric_claims):
    return sum([len([x for x in row if x > 1])
                for row in fabric_claims])


if __name__ == "__main__":
    size = 1000
    fabric_claims = [[0] * size for row in range(size)]

    claims = [transform_claim(x) for x in input.split('\n') if len(x) > 0]
    for claim in claims:
        fabric_claims = update_fabric_claims(fabric_claims, claim)

    print(count_overlap(fabric_claims))


"""
[[0, 0, 0],
 [1, 2, 2],
 [1, 2, 2]]

#1 @ 1,1: 2x2
#2 @ 0,1: 3x1
#123 @ 3,2: 5x4

"""
