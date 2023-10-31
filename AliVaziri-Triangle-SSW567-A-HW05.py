def classify_triangle(a, b, c):


    if not all(isinstance(n, int) for n in (a, b, c)):
        return "InvalidInput"

    if any(n < 0 or n > 200 for n in (a, b, c)):
        return "InvalidInput"

    if a >= b + c or b >= a + c or c >= a + b:
        return "NotATriangle"


    if a == b == c:
        return "Equilateral"
    elif a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2:
        return "Right"
    elif a != b and b != c and a != c:
        return "Scalene"
    else:
        return "Isosceles"
