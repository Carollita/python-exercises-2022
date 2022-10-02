matrix = [
    [1, 'a', 2],
    ['b', 3, 4],
    [5, 6, 'c'],
]

print(matrix)
# [[1, 'a', 2], ['b', 3, 4], [5, 6, 'c']]

print(matrix[0])
# [1, 'a', 2]

print(matrix[0][0])
# 1

print(matrix[0][-1])
# 2

print(matrix[-1][-1])
# c

# Tuple
another_matrix = (
    (5, 'c', 4),
    ('w', 2, 9),
    (0, 1, 'j'),
)

print(another_matrix)
# ((5, 'c', 4), ('w', 2, 9), (0, 1, 'j'))

print(another_matrix[0])
# (5, 'c', 4)