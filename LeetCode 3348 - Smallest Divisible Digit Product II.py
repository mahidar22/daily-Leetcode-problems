"""
=========================================================
LeetCode 3348 - Smallest Divisible Digit Product II
=========================================================

Problem
-------

You are given

1. A string num representing a positive integer.
2. An integer t.

Find the SMALLEST number that

1. Is greater than or equal to num.
2. Contains NO digit '0'.
3. The product of its digits is divisible by t.

If no such number exists,
return "-1".

---------------------------------------------------------

Example

num = "123"

t = 6

Digit product

1 × 2 × 3 = 6

Already divisible by 6.

Answer

"123"

---------------------------------------------------------

Example

num = "123"

t = 8

Current product

1 × 2 × 3 = 6

6 is not divisible by 8.

Need to find the next smallest valid number.

=========================================================
Observation
=========================================================

Digits can only be

1 2 3 4 5 6 7 8 9

No zeros are allowed.

The product of digits can only contain
prime factors

2
3
5
7

If t contains any other prime factor,
it is impossible.

=========================================================
Step 1
Check if Answer is Possible
=========================================================

temp = t

Divide temp by every digit

2 to 9

until no longer divisible.

Example

t = 72

72

÷2 =36

÷2 =18

÷2 =9

÷3 =3

÷3 =1

Possible.

----------------------------

Example

t =11

Cannot divide by

2..9

Still

11

Impossible.

Return "-1"

=========================================================
Step 2
Build Prefix Information
=========================================================

rem[i]

means

Remaining divisor still needed
after using the first i digits.

Initially

rem[0]=t

Suppose

num="236"

t=24

Digit 2

gcd(24,2)=2

Remaining

24/2=12

Digit3

gcd(12,3)=3

Remaining

12/3=4

Digit6

gcd(4,6)=2

Remaining

4/2=2

So

rem

24

12

4

2

Since final remaining

!=1

Current number isn't valid.

=========================================================
Why use gcd?
=========================================================

Suppose

Need

24

Current digit

6

Digit contributes

2×3

Need

24=2³×3

Digit removes only one

2

and one

3

Common part

gcd(24,6)=6

Remaining

24/6=4

Only

2²

still needed.

=========================================================
Step 3
If Already Valid
=========================================================

If

rem[n]==1

Every required factor is already present.

Return

num

=========================================================
Step 4
Modify Digits
=========================================================

Now we try making the number larger.

Start from

rightmost digit.

Increase it.

Then rebuild all digits after it
using the LARGEST possible digits.

Why?

Because

Large digits

remove more factors.

Need fewer changes.

Eventually

we obtain the smallest valid number.

=========================================================
Step 5
If Same Length Fails
=========================================================

Suppose

999

cannot become valid.

Need a longer number.

Construct the smallest longer number.

Factorize

t

into

9

8

7

...

2

Store them.

Then fill remaining positions

with

1

Reverse the string.

That gives the smallest answer.

=========================================================
Dry Run
=========================================================

num

123

t

8

--------------------------------

Current product

6

Need

8

Not enough.

--------------------------------

Try changing last digit

3→4

Now

124

Product

8

Divisible.

Return

124

=========================================================
Time Complexity
=========================================================

n = length of num

Building rem

O(n)

Trying modifications

O(9n)

Overall

O(n)

=========================================================
Space Complexity
=========================================================

rem array

O(n)

=========================================================
Python Solution
=========================================================
"""

import math


class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        temp = t
        for i in range(2, 10):
            while temp % i == 0:
                temp //= i

        if temp > 1:
            return "-1"

        n = len(num)
        rem = [0] * (n + 1)
        rem[0] = t
        pos = n - 1

        num_list = list(num)
        for i in range(n):
            if num_list[i] == "0":
                pos = i
                break
            rem[i + 1] = rem[i] // math.gcd(rem[i], int(num_list[i]))

        if rem[n] == 1:
            return num

        for i in range(pos, -1, -1):
            while True:
                num_list[i] = chr(ord(num_list[i]) + 1)
                if num_list[i] > "9":
                    break

                t_now = rem[i] // math.gcd(rem[i], int(num_list[i]))
                k = 9

                for j in range(n - 1, i, -1):
                    while t_now % k != 0:
                        k -= 1
                    t_now //= k
                    num_list[j] = str(k)

                if t_now == 1:
                    return "".join(num_list)

        ans = []
        original_t = t
        for i in range(9, 1, -1):
            while original_t % i == 0:
                ans.append(str(i))
                original_t //= i

        ans_str = "".join(ans)
        padding = max(n + 1 - len(ans_str), 0)
        ans_str += "1" * padding

        return ans_str[::-1]


# -------------------------------------------------------
# Example Usage
# -------------------------------------------------------

if __name__ == "__main__":

    s = Solution()

    print(s.smallestNumber("123", 6))   # 123
    print(s.smallestNumber("123", 8))   # 124