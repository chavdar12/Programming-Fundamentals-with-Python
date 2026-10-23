from math import floor, hypot


def center_point(a, a1, b, b1):
    a_result = hypot(a, a1)
    b_result = hypot(b, b1)
    if b_result < a_result:
        return b, b1, a, a1
    return a, a1, b, b1


def longer_line(a, a1, a2, a3, b, b1, b2, b3):
    a_line = hypot(a - a2, a1 - a3)
    b_line = hypot(b - b2, b1 - b3)
    if a_line >= b_line:
        return a, a1, a2, a3
    return b, b1, b2, b3


x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())
x3, y3 = float(input()), float(input())
x4, y4 = float(input()), float(input())
x, y, z, n = longer_line(x1, y1, x2, y2, x3, y3, x4, y4)
x, y, z, n = center_point(x, y, z, n)
print(f"({floor(x)}, {floor(y)})({floor(z)}, {floor(n)})")
