def howManyGrids(m, n, k):
    visited = [[False] * n for _ in range(m)]
    return backTrace(0, 0, m, n, k, visited)


def backTrace(row, col, m, n, k, visited):
    count = 0
    for i in range(row, m):
        for j in range(col, n):
            if judgeEnter(i, j, m, n, k, visited):
                visited[i][j] = True
                count = 1 + backTrace(row - 1, col, m, n, k, visited) + \
                        backTrace(row + 1, col, m, n, k, visited) + \
                        backTrace(row, col - 1, m, n, k, visited) + \
                        backTrace(row, col + 1, m, n, k, visited)
    return count


def judgeEnter(i, j, m, n, k, visited):
    if i < 0 or j < 0 or i >= m or j >= n or visited[i][j]:
        return False

    sum = 0
    while i > 0:
        pop = i % 10
        sum += pop
        i = i // 10

    while j > 0:
        pop = j % 10
        sum += pop
        j = j // 10

    if sum > k:
        return False
    else:
        return True


if __name__ == '__main__':
    print(howManyGrids(3, 4, 3))
