def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """

    for row in matrix:

        for col in row:
            print(col)
        print()

if __name__ == "__main__":
    matrix = [[1, 3, 5, 7],
              [10, 11, 16, 20],
              [23, 30, 34, 60]]

    searchMatrix(matrix, 3)