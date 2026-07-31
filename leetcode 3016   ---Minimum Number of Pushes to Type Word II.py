"""
=========================================================
LeetCode 3016 - Minimum Number of Pushes to Type Word II
=========================================================

Problem
-------
You are given a string 'word'.

There is a phone keypad with 8 keys that can store letters.
Each key can contain any number of letters.

Typing Rule
-----------
If a letter is

1st letter on a key -> 1 push
2nd letter on a key -> 2 pushes
3rd letter on a key -> 3 pushes
...

You can arrange the letters on the keypad in ANY order before typing.

Goal
----
Find the minimum number of pushes required to type the given word.

---------------------------------------------------------

Example 1

word = "abcde"

There are only 5 unique letters.

Since there are 8 keys,
put each letter on a different key.

a -> Key1 (1 push)
b -> Key2 (1 push)
c -> Key3 (1 push)
d -> Key4 (1 push)
e -> Key5 (1 push)

Total pushes = 5

---------------------------------------------------------

Example 2

word = "xycdefghij"

Unique letters = 10

Only first 8 letters can be placed in first position.

Those cost 1 push.

Remaining 2 letters become second letter
on some keys.

Those cost 2 pushes.

---------------------------------------------------------

Important Observation
---------------------

We can arrange letters however we want.

Therefore,

Most frequent letters should require fewer pushes.

Least frequent letters can require more pushes.

This is a Greedy problem.

---------------------------------------------------------

Why?

Suppose

a appears 100 times
b appears 2 times

If

a needs 2 pushes
b needs 1 push

Total

100×2 + 2×1 = 202

Swap them

a ->1 push
b ->2 pushes

100×1 + 2×2 =104

Much smaller.

Hence

Higher frequency letters should always get lower push cost.

---------------------------------------------------------

Idea

Step 1
Count frequency of every character.

Example

word = "aaabbcc"

Frequency

a = 3
b = 2
c = 2

---------------------------------------------------------

Step 2

Sort frequencies in descending order.

[3,2,2]

---------------------------------------------------------

Step 3

Assign push costs.

There are 8 keys.

First 8 frequencies
cost = 1

Next 8
cost = 2

Next 8
cost = 3

...

---------------------------------------------------------

Why

There are only 8 first positions.

After filling them,

next letters become second position.

---------------------------------------------------------

Formula

If i is index

0 1 2 3 4 5 6 7

cost = 1

8 9 10 ...

cost = 2

16...

cost =3

Formula

cost = i // 8 + 1

---------------------------------------------------------

Dry Run

word = "aabbccddeeffgghhiij"

Frequencies

a=2
b=2
c=2
d=2
e=2
f=2
g=2
h=2
i=2
j=1

Sorted

[2,2,2,2,2,2,2,2,2,1]

Now assign costs

Index 0
cost =1
2×1=2

Index 1
cost =1
2×1=2

Index 2
cost =1
2×1=2

Index 3
cost =1
2×1=2

Index 4
cost =1
2×1=2

Index 5
cost =1
2×1=2

Index 6
cost =1
2×1=2

Index 7
cost =1
2×1=2

Total so far =16

Index 8

cost =2

2×2=4

Total=20

Index9

cost=2

1×2=2

Final Answer=22

---------------------------------------------------------

Time Complexity

Counter -> O(n)

Sorting frequencies

If k is number of unique letters

O(k log k)

Since English letters are only 26,

sorting is effectively constant.

Overall

O(n)

---------------------------------------------------------

Space Complexity

Counter stores at most 26 letters.

O(1)

---------------------------------------------------------

Python Solution
---------------------------------------------------------
"""

from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        # Count frequency of each character
        freq = sorted(Counter(word).values(), reverse=True)

        ans = 0

        # Assign push costs
        for i, f in enumerate(freq):
            ans += (i // 8 + 1) * f

        return ans


# ----------------------------
# Example Usage
# ----------------------------
if __name__ == "__main__":
    s = Solution()

    print(s.minimumPushes("abcde"))          # Output: 5
    print(s.minimumPushes("xycdefghij"))     # Example with 10 unique letters
    print(s.minimumPushes("aabbccddeeff"))   # Example with repeated letters
