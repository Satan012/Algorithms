def findPath(grid, path):
    col = row = 0

    return backtrace(row, col, grid, path)


def backtrace(row, col, grid, path):
    if len(path) == 0:
        return True

    for i in range(col, len(grid[0])):
        if grid[row][i] == path[0]:
            tmp1 = tmp2 = tmp3 = False
            if row + 1 < len(grid):
                tmp1 = backtrace(row + 1, i, grid, path[1:])
            if col + 1 < len(grid[0]):
                tmp2 = backtrace(row, i + 1, grid, path[1:])
            if col == len(grid[0]) - 1 and row == len(grid) - 1 and grid[row][col] == path[0]:
                tmp3 = True
            if tmp1 or tmp2 or tmp3:
                return True
    return False


if __name__ == '__main__':
    grid = [
        ['a', 'b', 't', 'g'],
        ['c', 'f', 'c', 's'],
        ['j', 'd', 'e', 'h']
    ]

    path = 'abfceh'

    print(findPath(grid, path))
