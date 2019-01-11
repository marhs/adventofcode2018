from collections import Counter


input = open('input.txt', 'r').read()
test_string = 'babbc'


# Map
def count_word(word):
    values = set(Counter(word).values())
    return (2 in values, 3 in values)


# Reduce
def calculate_checksum(ids):
    checksum = [0, 0]
    for processed_id in ids:
        if processed_id[0]:
            checksum[0] += 1
        if processed_id[1]:
            checksum[1] += 1
    return checksum[0] * checksum[1]


if __name__ == "__main__":
    ids = [count_word(x) for x in input.split()]
    print(calculate_checksum(ids))


"""
             2  3
'abcdef' -> ( ,  )
'bababc' -> (x, x)
'abbcde' -> (x,  )
'abcccd' -> ( , x)
'aabcdd' -> (x,  )
'abcdee' -> (x,  )
'ababab' -> ( , x)
---
Total ->    (4, 3)
"""
