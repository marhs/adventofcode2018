from string import ascii_lowercase


def check_reaction(a, b):
    """Given two units, check if they react"""
    return (a.lower() == b.lower()) and (a != b)


def chain_reactions_recursive(input, current_index=0):
    """
    Doesn't work with current python recursive conditions
    """
    for index in range(current_index, len(input)-1):
        a, b = input[index], input[index+1]
        if check_reaction(a, b):
            print(len(input), index)
            new_input = input[:index] + input[index+2:]
            new_index = max(0, index-1)
            return chain_reactions(new_input, current_index=new_index)
    return len(input)


def chain_reactions(input, index=0):
    # Stop condition
    while(True):
        if index == len(input) - 1:
            return len(input)

        a, b = input[index], input[index+1]

        if check_reaction(a, b):
            input = input[:index] + input[index+2:]
            index = max(0, index-1)
            continue

        index += 1


def generate_polymer_combinations(input):
    res = {}
    for letter in ascii_lowercase:
        new_input = input.replace(letter, '')
        new_input = new_input.replace(letter.upper(), '')
        res[letter] = chain_reactions(new_input)
    return min(res.items(), key=lambda x: x[1])


if __name__ == '__main__':
    filename = 'input.txt'
    input = open(filename, 'r').read()[:-1]
    # Part A
    print(chain_reactions(input))
    # Part B
    print(generate_polymer_combinations(input))
