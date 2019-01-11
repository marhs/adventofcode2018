input = open('input.txt', 'r').read()


def separate_steps(string):
    return sum([int(x) for x in string.split()])


if __name__ == "__main__":
    print(separate_steps(input))
