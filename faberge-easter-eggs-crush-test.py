from functools import cache

@cache
def height(n: int, m: int) -> int:
    if n == 0 or m == 0:
        return 0
    
    if n == 1:
        return m
    
    if n == 2:
        return m * (m + 1) // 2
    
    ans = 0
    for i in range(m):
        ans += height(n - 1, i) + 1
    
    return ans
