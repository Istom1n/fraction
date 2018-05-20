"""
Splits a fraction to
Numerator and Denominator
Using the Continued fraction method

Written by: Ivan Istomin
Date: 20.05.2018

So said to do Guido: PEP 484 (https://www.python.org/dev/peps/pep-0484/)
"""

from numpy import matrix


def get_num_dem(fraction: float) -> (int, int):
    """
    Splits a fraction to Numerator and Denominator,
    but Num abd Den returned in abbreviated form

    :param fraction: Fraction you want to split
    :return: Numerator and Denominator of your Fraction
    """
    a_i = 0
    sign = 1

    m = matrix('1 0; 0 1')

    if fraction < 0.0:
        # Work in positive space, it seems we can get confused by negatives
        sign = -1
        fraction *= -1.0

    x = fraction
    count = 0

    # Loop finding terms until denominator gets too big
    while m[1, 0] * a_i + m[1, 1] <= 1000:
        a_i = int(x)

        t = m[0, 0] * a_i + m[0, 1]
        m[0, 1] = m[0, 0]
        m[0, 0] = t
        t = m[1, 0] * a_i + m[1, 1]
        m[1, 1] = m[1, 0]
        m[1, 0] = t

        if x == float(a_i):
            break

        x = 1 / (x - float(a_i))

        # math.inf & float('int') didn't work properly
        if x > float(0x7FFFFFFF):
            break

    num = m[0, 0] * sign
    den = m[1, 0]
    err = fraction - float(m[0, 0]) / float(m[1, 0])

    # print('Error:', err)

    return num, den


# Example 1
number, demon = get_num_dem(1 / 3)
print('Num: {}, Dem: {};'.format(number, demon))
assert number == 1 and demon == 3, 'Error in the first example'

# Example 2
number, demon = get_num_dem(5 / 12)
print('Num: {}, Dem: {};'.format(number, demon))
assert number == 5 and demon == 12, 'Error in the second example'

# Example 3
number, demon = get_num_dem(34 / 354)
print('Num: {}, Dem: {};'.format(number, demon))
assert number == 17 and demon == 177, 'Error in the third example'  # Reduced fraction
