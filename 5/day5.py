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


if __name__ == '__main__':
    filename = 'input.txt'
    input = open(filename, 'r').read()[:-1]
    print(chain_reactions(input))


"""
dabAcCaCBAcCcaDA
     x

dabAaCBAccaDA
   vx

dabCBAcaDA
     vx

var1 = A

bBaA

bB
"""
