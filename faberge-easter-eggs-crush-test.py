def height(n: int, m: int) -> int:
    # Recurrence relation:
    # F(n, m) = F(n - 1, m - 1) + 1 + F(n, m - 1)

    if n == 0 or m == 0:
        return 0

    prv = [0 for _ in range(m + 1)]
    cur = [0 for _ in range(m + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cur[j] = prv[j - 1] + 1 + cur[j - 1]
        prv = cur[:]

    return cur[m]
