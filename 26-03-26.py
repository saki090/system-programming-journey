import time
# Now I am going to define 3x3 matrices using lists of lists.

mat_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

start = time.perf_counter()

for i in range(3):
    for j in range(3):
        for k in range(3):
            result[i][j] += mat_a[i][k] * mat_b[k][j]

end = time.perf_counter()

print("Result matrix:")
for row in result:
    print(row)
print(f"Time taken: {end - start} seconds")
