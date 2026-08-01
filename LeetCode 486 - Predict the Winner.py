"""
=========================================================
LeetCode 486 - Predict the Winner
=========================================================

Problem
-------

You are given an integer array nums.

Two players (Player 1 and Player 2) play a game.

Rules
-----

1. Both players play optimally.
2. On each turn, a player can only pick
   - the leftmost number
   - OR the rightmost number.
3. The chosen number is added to the player's score.
4. Continue until no numbers remain.

Return

True  -> if Player 1 can win or tie.
False -> otherwise.

A tie is also considered a win for Player 1.

---------------------------------------------------------

Example 1

nums = [1,5,2]

Player 1 choices

Pick 1

Remaining

[5,2]

Player 2 picks 5

Player 1 gets 2

Scores

Player1 = 3
Player2 = 5

----------------

Pick 2

Remaining

[1,5]

Player2 picks 5

Player1 gets 1

Scores

Player1 = 3
Player2 = 5

Player1 loses.

Answer = False

---------------------------------------------------------

Example 2

nums = [1,5,233,7]

Player1 picks 1

Player2 picks 5

Player1 picks 233

Player2 picks 7

Scores

Player1 = 234
Player2 = 12

Player1 wins.

Answer = True

=========================================================
Observation
=========================================================

Every turn,

a player has only TWO choices.

1. Pick left
2. Pick right

Both players always choose the BEST move.

This immediately suggests

Dynamic Programming (DP).

=========================================================
Key Idea
=========================================================

Instead of calculating

Player1 score
Player2 score

we calculate

Score Difference

difference = CurrentPlayerScore - OpponentScore

Suppose

difference > 0

Current player can finish with a higher score.

difference = 0

Tie.

difference < 0

Current player loses.

=========================================================
State Definition
=========================================================

dp(i, j)

means

Maximum score difference the current player can obtain
from subarray

nums[i...j]

=========================================================
Choices
=========================================================

Current player has two choices.

--------------------------------

Choice 1

Take left element

nums[i]

Opponent now plays

dp(i+1, j)

Since opponent's advantage becomes our disadvantage,

Difference

nums[i] - dp(i+1, j)

--------------------------------

Choice 2

Take right element

nums[j]

Difference

nums[j] - dp(i, j-1)

--------------------------------

Take maximum

dp(i,j)=max(
    nums[i]-dp(i+1,j),
    nums[j]-dp(i,j-1)
)

=========================================================
Base Case
=========================================================

If

i == j

Only one number remains.

Current player takes it.

dp(i,i)=nums[i]

=========================================================
Dry Run
=========================================================

nums = [1,5,2]

Need

dp(0,2)

--------------------------------

Take Left

1 - dp(1,2)

Compute dp(1,2)

Take 5

5-2=3

Take2

2-5=-3

Maximum=3

So

1-3=-2

--------------------------------

Take Right

2-dp(0,1)

dp(0,1)

Take1

1-5=-4

Take5

5-1=4

Maximum=4

So

2-4=-2

--------------------------------

Maximum

max(-2,-2)

=-2

Negative means

Player1 loses.

Return False.

=========================================================
Another Dry Run
=========================================================

nums = [1,5,233,7]

Eventually

dp(0,3)=222

Positive

Player1 wins.

Return True.

=========================================================
Time Complexity
=========================================================

There are

n*n

states.

Each state takes O(1).

Time

O(n²)

=========================================================
Space Complexity
=========================================================

Memoization table

O(n²)

=========================================================
Python Solution (Memoization)
=========================================================
"""

from functools import lru_cache
from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        @lru_cache(None)
        def dp(left, right):

            # Only one element left
            if left == right:
                return nums[left]

            # Pick left
            choose_left = nums[left] - dp(left + 1, right)

            # Pick right
            choose_right = nums[right] - dp(left, right - 1)

            # Best possible score difference
            return max(choose_left, choose_right)

        # Player1 wins or ties
        return dp(0, len(nums) - 1) >= 0


# -------------------------------------------------------
# Example Usage
# -------------------------------------------------------

if __name__ == "__main__":

    s = Solution()

    print(s.PredictTheWinner([1, 5, 2]))          # False
    print(s.PredictTheWinner([1, 5, 233, 7]))     # True