""" rotate the given matrix by 90 degress anti clock wise problem
1. take transpose of that matrix (swap rows and columns)
2. reverse each column (instead of reversing rows as we do for the clockwise)

"""
# Function to rotate matrix by 90 degrees anti-clockwise
def rotate_matrix(arr, N):
    # Step 1: Transpose
    for i in range(N):
        for j in range(i, N):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    # Step 2: Reverse each column
    for j in range(N):
        for i in range(N // 2):
            arr[i][j], arr[N - 1 - i][j] = arr[N - 1 - i][j], arr[i][j]

    return arr


# Input handling
N = int(input().strip())
nums = list(map(int, input().split()))

# Convert flat list into NxN matrix
matrix = [nums[i * N:(i + 1) * N] for i in range(N)]

# Rotate
rotated = rotate_matrix(matrix, N)

# Print result
for row in rotated:
    print(" ".join(map(str, row)))

