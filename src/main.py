def isMagicSquare(matrix, rows, cols):
    # For matrix which isn't square
    if (rows != cols):
        return False

    # Declaring variables
    rowSum = 0
    colSum = 0
    temp = 0

    # Checking Horizontal and Vertical Sum
    for i in range(0, rows):
        for j in range(0, cols):
            rowSum += matrix[i][j]
            colSum += matrix[j][i]
        if (i == 0 and rowSum == colSum):
            temp = rowSum
            rowSum = 0
            colSum = 0
        elif (temp != 0 and temp == rowSum and temp == colSum):
            rowSum = 0
            colSum = 0
        else:
            return False

    # Checking Diagonal Sum
    for i in range(0, rows):
        for j in range(0, cols):
            if (i == j):
                rowSum += matrix[i][j]
            if (j == cols - i - 1):
                colSum += matrix[i][j]
    if (rowSum == temp and colSum == temp):
        return True
    return False


# Main function calling
matrix = [[8, 11, 14, 1],
          [13, 2, 7, 12],
          [3, 16, 9, 6],
          [10, 5, 4, 15]]
rows = len(matrix)
cols = len(matrix[0])
print(isMagicSquare(matrix, rows, cols))