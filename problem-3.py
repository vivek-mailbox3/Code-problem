"""
Question 3:
Given an m x n integers matrix, return the length of the longest increasing path in matrix.
From each cell, you can either move in four directions: left, right, up, or down. You may not
move diagonally or move outside the boundary (i.e., wrap-around is not allowed).
"""


def longest_increasing_path(matrix):
    """
    Returns the length of the longest increasing path in the given matrix.
    """
    rows, cols = len(matrix), len(matrix[0])
    dp_table = [[0] * cols for _ in range(rows)]

    def dfs(row_index, col_index):
        # If the result for this position is already computed, return it
        if dp_table[row_index][col_index] > 0:
            return dp_table[row_index][col_index]

        longest_path = 1
        current_val = matrix[row_index][col_index]

        directions = (
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        )  # four directions to explore: right, left, down, up.

        for dx, dy in directions:
            neighbor_row, neighbor_col = row_index + dx, col_index + dy
            if (
                0 <= neighbor_row < rows
                and 0 <= neighbor_col < cols
                and matrix[neighbor_row][neighbor_col] > current_val
            ):
                longest_path = max(longest_path, dfs(neighbor_row, neighbor_col) + 1)
                # Compute the longest increasing path starting from the new position and update the result.

        dp_table[row_index][col_index] = longest_path

        return longest_path

    longest_path_length = 0
    for i in range(rows):
        for j in range(cols):
            longest_path_length = max(longest_path_length, dfs(i, j))

    return longest_path_length


if __name__ == "__main__":
    # matrix = [[1]]
    matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    print(longest_increasing_path(matrix))

