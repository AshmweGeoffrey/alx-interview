#!/usr/bin/python3
"""
0-pascal_triangle
"""
def pascal_triangle(n):
    """Define pascal_triangle function.
    Description:
                This function will return a list of integers
                representing the pascal's triangle of n.

                It will return an empty list if n <= 0.
                We assume n will always be an integer.
    """

    if n <= 0:
        return []  # Return an empty list for invalid input

    init_list = [[1], [1, 1]]  # The initial values in Pascal's Triangle

    for i in range(2, n):
        row = [1]  # Each row starts with 1

        # Generate the rest of the row
        for j in range(1, i):
            row.append(init_list[i - 1][j - 1] + init_list[i - 1][j])

        row.append(1)  # Each row ends with 1
        init_list.append(row)

    return init_list
