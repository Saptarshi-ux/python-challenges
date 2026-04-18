"""Given an integer n where 3 < n < 10^9, determine the minimum number of perfect square numbers required to sum exactly to n. 
A perfect square is any integer of the form k², such as 1, 4, 9, 16, and so on. 
For example, 17 can be written as 16 + 1, so the answer is 2, while 16 is itself a perfect square, 
so the answer is 1. Some numbers require more terms: 15 = 9 + 4 + 1 + 1, and 
it cannot be expressed as the sum of only three perfect squares, so the answer is 4. 
Since the input range can be as large as 10^9, a brute-force approach will not be efficient enough; 
the challenge is to design an algorithm that computes the answer quickly even for very large values of n."""

import math
def sum_of_squares(n):
    if math.isqrt(n)**2 == n: return 1
    temp = n
    while temp % 4 == 0: temp //= 4
    if temp % 8 == 7: return 4
    for i in range(1, int(math.sqrt(n)) + 1):
        remainder = n - i*i
        if math.isqrt(remainder)**2 == remainder:
            return 2
    return 3
