from sympy import symbols, sympify

def parse_equation(eq_str):
    # Define symbols
    u, v = symbols('u v')
    # Initialize coefficients
    a1 = a2 = a3 = a4 = a6 = 0

    # Convert the equation string into a symbolic expression
    eq_str = eq_str.replace("=", "-(") + ")"
    eq_str = eq_str.replace("^", "**")
    equation = sympify(eq_str, locals={'u': u, 'v': v})

    # Extract terms and coefficients
    coeffs = equation.as_coefficients_dict()

    for term, coeff in coeffs.items():
        if term == u*v:
            a1 = coeff
        elif term == v:
            a3 = coeff
        elif term == u**2:
            a2 = -coeff
        elif term == u:
            a4 = -coeff
        elif term == 1:
            a6 = -coeff

    return a1, a2, a3, a4, a6

def calculate_constant_values(a1, a2, a3, a4, a6):
    b2 = a1**2 + 4*a2
    b4 = a1*a3 + 2*a4
    b6 = a3**2 + 4*a6
    b8 = a1**2*a6 + 4*a2*a6 - a1*a3*a4 + a2*a3**2 - a4**2

    c4 = b2**2 - 24*b4
    c6 = -b2**3 + 36*b2*b4 - 216*b6

    delta = -b2**2*b8 - 8*b4**3 - 27*b6**2 + 9*b2*b4*b6

    j = float(c4**3/delta) if delta != 0 else None

    return b2, b4, b6, b8, c4, c6, delta, j


if __name__ == '__main__':
    
    # Example input
    eq_str = "v^2 + 2*u*v + 3*v = u^3 + 13*u^2 + 14*u + 17"
    eq_str = "v^2 = u^3 + u^2"
    eq_str = "v^2 + v = u^3"
    eq_str = "v^2= u^3 + u"

    a1, a2, a3, a4, a6 = parse_equation(eq_str)
    const_values = calculate_constant_values(a1, a2, a3, a4, a6)

    print(f"Given equation: {eq_str}")
    print(f"a1: {a1}, a2: {a2}, a3: {a3}, a4: {a4}, a6: {a6}")
    print(f"b2: {const_values[0]}, b4: {const_values[1]}, b6: {const_values[2]}, b8: {const_values[3]}, c4: {const_values[4]}, c6: {const_values[5]}, delta: {const_values[6]}, j: {const_values[7]}")
