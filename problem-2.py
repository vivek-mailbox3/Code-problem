"""
Question 2:
You are given an n x n 2D matrix representing an image, rotate the image by 90
degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D
matrix directly. DO NOT allocate another 2D matrix and do the rotation.	
"""

	
def rotate(matrix):
    n = len(matrix)

    # Transpose
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse row
    for i in range(n):
        matrix[i] = matrix[i][::-1]

    return matrix


if __name__ == "__main__":
    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    print(rotate(matrix))

