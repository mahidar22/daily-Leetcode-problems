"""
=========================================================
LeetCode 1406 - Stone Game III
=========================================================

Problem
-------

Alice and Bob are playing a game.

There is an array

stoneValue

Each element represents the value of a stone.

Example

stoneValue = [1,2,3,7]

Rules
-----

1. Alice starts first.
2. Players play alternately.
3. On each turn, a player can take

   - 1 stone
   - 2 stones
   - 3 stones

   from the FRONT of the array.

4. The value of the taken stones is added
   to the player's score.

5. Both players play optimally.

Return

"Alice" -> Alice gets more score.
"Bob"   -> Bob gets more score.
"Tie"   -> Scores are equal.

---------------------------------------------------------

Example 1

stoneValue = [1,2,3,7]

Alice takes

1+2+3 = 6

Bob takes

7

Alice = 6

Bob = 7

Answer

Bob

---------------------------------------------------------

Example 2

stoneValue = [1,2,3,-9]

Alice takes

1+2+3 = 6

Bob takes

-9

Alice = 6

Bob = -9

Answer

Alice

=========================================================
Observation
=========================================================

Every turn,

Current player has only

3 choices.

Take

1 stone

or

2 stones

or

3 stones.

After taking stones,

the opponent plays optimally.

This is a Dynamic Programming problem.

=========================================================
Key Idea
=========================================================

Instead of storing

Alice score
Bob score

store

Score Difference

difference

=

Current Player Score
-
Opponent Score

Positive

Current player wins.

Negative

Opponent wins.

Zero

Tie.

=========================================================
DP State
=========================================================

dp(i)

=

Maximum score difference

(Current Player - Opponent)

starting from

index i

=========================================================
Transition
=========================================================

Current player can take

1

or

2

or

3 stones.

Suppose

takeSum

=

sum of stones taken.

Opponent starts from

i+k

Opponent's advantage

=

dp(i+k)

Therefore

Current player's advantage

=

takeSum - dp(i+k)

Take the maximum.

=========================================================

Formula

dp(i)

=

max(

take1 - dp(i+1),

take2 - dp(i+2),

take3 - dp(i+3)

)

=========================================================
Base Case
=========================================================

If

i >= n

No stones remain.

Difference

0

=========================================================
Dry Run
=========================================================

stoneValue

=

[1,2,3,7]

Need

dp(0)

----------------------------------

Take 1

Gain

1

Difference

1 - dp(1)

----------------------------------

Take 2

Gain

3

Difference

3 - dp(2)

----------------------------------

Take 3

Gain

6

Difference

6 - dp(3)

DP computes all possibilities.

Eventually

dp(0)

=

-1

Negative

Bob wins.

=========================================================
Another Example
=========================================================

stoneValue

=

[1,2,3,-9]

Eventually

dp(0)

=

15

Positive

Alice wins.

=========================================================
Time Complexity
=========================================================

Each index

computed once.

Each state tries

3 moves.

Time

O(n)

=========================================================
Space Complexity
=========================================================

Memoization

O(n)

=========================================================
Python Solution
=========================================================
"""

from functools import lru_cache
from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        n = len(stoneValue)

        @lru_cache(None)
        def dp(i):

            # No stones left
            if i >= n:
                return 0

            best = float("-inf")
            takeSum = 0

            # Try taking 1, 2, or 3 stones
            for k in range(3):

                if i + k < n:
                    takeSum += stoneValue[i + k]
                    best = max(best, takeSum - dp(i + k + 1))

            return best

        difference = dp(0)

        if difference > 0:
            return "Alice"

        elif difference < 0:
            return "Bob"

        return "Tie"


# -------------------------------------------------------
# Example Usage
# -------------------------------------------------------

if __name__ == "__main__":

    s = Solution()

    print(s.stoneGameIII([1,2,3,7]))      # Bob
    print(s.stoneGameIII([1,2,3,-9]))     # Alice
    print(s.stoneGameIII([1,2,3,6]))      # Tie