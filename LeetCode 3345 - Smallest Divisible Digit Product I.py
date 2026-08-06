"""
=========================================================
LeetCode 3345 - Smallest Divisible Digit Product I
=========================================================

Problem
-------

You are given two integers

n
t

Find the smallest integer x such that

1. x >= n
2. Product of digits of x is divisible by t

Return x.

---------------------------------------------------------

Example 1

Input

n = 10
t = 2

Check

10

Digits

1, 0

Product

1 × 0 = 0

0 is divisible by 2.

Answer

10

---------------------------------------------------------

Example 2

Input

n = 15
t = 3

Check

15

Product

1 × 5 = 5

5 % 3 != 0

----------------

16

1 × 6 = 6

6 % 3 == 0

Answer

16

=========================================================
Observation
=========================================================

The constraints are small.

We can simply check every number starting from n.

For each number,

1. Find the product of its digits.
2. Check if product % t == 0.

The first number satisfying the condition
is the answer.

=========================================================
Algorithm
=========================================================

Start from x = n

Repeat forever

    Compute product of digits of x

    If

    product % t == 0

        return x

    Else

        x += 1

=========================================================
Finding Product of Digits
=========================================================

Suppose

x = 248

Digits

2

4

8

Product

2 × 4 × 8

=

64

Use

while num > 0

digit = num % 10

product *= digit

num //= 10

=========================================================
Special Case
=========================================================

If any digit is

0

Product becomes

0

Since

0 % t == 0

the number automatically satisfies the condition.

Example

105

Product

1 × 0 × 5

=

0

=========================================================
Dry Run
=========================================================

n = 15

t = 3

----------------

Check

15

Product

1 × 5 = 5

5 % 3 != 0

Not valid.

----------------

Check

16

Product

1 × 6 = 6

6 % 3 == 0

Return

16

=========================================================
Another Dry Run
=========================================================

n = 28

t = 5

Check

28

2 × 8 = 16

Not divisible.

----------------

29

2 × 9 = 18

Not divisible.

----------------

30

3 × 0 = 0

0 % 5 = 0

Return

30

=========================================================
Time Complexity
=========================================================

Suppose the answer is x.

We check

x - n + 1

numbers.

For each number,

we process all its digits.

Time

O((x - n) × digits)

=========================================================
Space Complexity
=========================================================

O(1)

=========================================================
Python Solution
=========================================================
"""


class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        while True:

            product = 1
            num = n

            # Calculate product of digits
            while num > 0:
                digit = num % 10
                product *= digit
                num //= 10

            # Check divisibility
            if product % t == 0:
                return n

            n += 1


# -------------------------------------------------------
# Example Usage
# -------------------------------------------------------

if __name__ == "__main__":

    s = Solution()

    print(s.smallestNumber(10, 2))   # 10
    print(s.smallestNumber(15, 3))   # 16
    print(s.smallestNumber(28, 5))   # 30
    