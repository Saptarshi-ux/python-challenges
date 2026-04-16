""" Create a function that differentiates a polynomial for a given value of x.
Your function will receive 2 arguments: a polynomial as a string, and a point to evaluate the equation as an integer."""

""" Assumptions:
There will be a coefficient near each x, unless the coefficient equals 1 or -1.
There will be an exponent near each x, unless the exponent equals 0 or 1.
All exponents will be greater or equal to zero"""
# the code is:
import re
def differentiate(poly, x):
    p = re.sub(r'(?<!\d)x', '1x', poly.replace('-x', '-1x'))
    return sum(int(a) * int(n or 1) * (x**(int(n or 1)-1)) 
               for a, n in re.findall(r'([+-]?\d+)x\^?(\d*)', p))
