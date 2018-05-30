"""
Splits a fraction to
Numerator and Denominator
Using the Continued fraction method

Written by: Ivan Istomin
Date: 20.05.2018

So said to do Guido:
PEP 484 (https://www.python.org/dev/peps/pep-0484/)
PEP 526 (https://www.python.org/dev/peps/pep-0526/)
"""

from typing import Tuple

from numpy import int64, matrix


def get_num_dem(fraction: float) -> Tuple[int64, int64]:
    """
    Splits a fraction to Numerator and Denominator,
    but Num abd Den returned in abbreviated form

    :param fraction: Fraction you want to split
    :return: Numerator and Denominator of your Fraction
    """
    a_i: int = 0
    sign: int = 1

    m: matrix = matrix('1 0; 0 1')

    if fraction < 0.0:
        # Work in positive space, it seems we can get confused by negatives
        sign = -1
        fraction *= -1.0

    x: float = fraction

    # Loop finding terms until denominator gets too big
    while m[1, 0] * a_i + m[1, 1] <= 1000:
        a_i = int(x)

        t: int = m[0, 0] * a_i + m[0, 1]
        m[0, 1] = m[0, 0]
        m[0, 0] = t

        t = m[1, 0] * a_i + m[1, 1]
        m[1, 1] = m[1, 0]
        m[1, 0] = t

        if x == float(a_i):
            break

        x = 1 / (x - float(a_i))

        # math.inf & float('inf') didn't work properly
        if x > float(0x7FFFFFFF):
            break

    num: int = m[0, 0] * sign
    den: int = m[1, 0]
    err: float = fraction - float(m[0, 0]) / float(m[1, 0])

    print('Error:', err)

    return num, den
