input = open('input.txt', 'r').read()
test_string = 'babbc'


def compare_strings(str_a, str_b):
    final_string = ""
    for i in range(len(str_a)):
        if str_a[i] == str_b[i]:
            final_string += str_a[i]
    return len(final_string) == len(str_a) - 1, final_string


def search_duplicates(ids):
    for id in ids:
        for id2 in ids:
            is_same, rest = compare_strings(id, id2)
            if is_same:
                return rest
    return False


if __name__ == "__main__":
    print(search_duplicates(input.split()))

"""
abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
"""
