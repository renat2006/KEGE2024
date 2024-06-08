def g(s, m):
    if s >= 301: return m % 2 == 0
    if m == 0: return 0
    mn = [g(s + 3, m - 1), g(s * 5, m - 1)]
    return any(mn) if (m - 1) % 2 == 0 else all(mn)


print(19, [s for s in range(1, 301) if g(s, 2)])
print(20, [s for s in range(1, 301) if not g(s, 1) and g(s, 3)])
print(21, [s for s in range(1, 301) if not g(s, 2) and g(s, 4)])