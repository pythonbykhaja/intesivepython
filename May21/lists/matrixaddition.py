matrix_1 = [[1,2,3], [4,5,6], [7,8,9]]
matrix_2 = [[10,11,12], [13,14,15], [16,17,18]]
result = [[0,0,0], [0,0,0], [0,0,0]]

row_count = len(matrix_1)
col_count = len(matrix_1[0])

for row in range(row_count):
    for col in range(col_count):
        result[row][col] = matrix_1[row][col] + matrix_2[row][col]

print(result)
