"""
=========================================================
LeetCode 877 - Stone Game
=========================================================

Problem
-------

Alice and Bob are playing a game.

There are several piles of stones.

Example

piles = [5,3,4,5]

Rules
-----

1. Alice starts first.
2. Alice and Bob play alternately.
3. On each turn, a player can take
      - the leftmost pile
      - OR the rightmost pile.
4. Whoever takes a pile gets all stones in it.
5. Total number of piles is even.
6. Total number of stones is odd.
   (So a tie is impossible.)

Both players always play optimally.

Return

True  -> Alice wins
False -> Bob wins

---------------------------------------------------------

Example

piles = [5,3,4,5]

Initially

[5,3,4,5]

Alice

Can take

Left = 5

or

Right = 5

Suppose Alice takes Left.

Remaining

[3,4,5]

Bob plays optimally.

Eventually

Alice wins.

Answer = True

=========================================================
Observation
=========================================================

This problem looks almost identical to
LeetCode 486 (Predict the Winner).

Difference

486
---
Player 1 wins OR ties.

877
---
Tie is impossible because

1. Total stones are odd.
2. Number of piles is even.

=========================================================
Key Idea
=========================================================

Instead of storing

Alice score
Bob score

store

Score Difference

difference =
Current Player Score - Opponent Score

If

difference > 0

Current player wins.

=========================================================
DP State
=========================================================

dp(left, right)

means

Maximum score difference
the current player can obtain
using

piles[left...right]

=========================================================
Choices
=========================================================

Current player has two choices.

--------------------------------

Choice 1

Take left pile

Gain

piles[left]

Opponent now plays

dp(left+1,right)

Final difference

piles[left] - dp(left+1,right)

--------------------------------

Choice 2

Take right pile

Difference

piles[right] - dp(left,right-1)

--------------------------------

Take maximum

dp(left,right)=max(
    piles[left]-dp(left+1,right),
    piles[right]-dp(left,right-1)
)

=========================================================
Base Case
=========================================================

Only one pile left.

Current player takes it.

dp(i,i)=piles[i]

=========================================================
Dry Run
=========================================================

piles = [5,3,4,5]

Need

dp(0,3)

--------------------------------

Choose Left

5 - dp(1,3)

--------------------------------

Choose Right

5 - dp(0,2)

DP recursively computes both possibilities.

Eventually

dp(0,3)=1

Positive

Alice wins.

Return True.

=========================================================
Time Complexity
=========================================================

States

n²

Each state

O(1)

Time

O(n²)

=========================================================
Space Complexity
=========================================================

Memoization

O(n²)

=========================================================
Python Solution (General DP)
=========================================================
"""

from functools import lru_cache
from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        @lru_cache(None)
        def dp(left, right):

            # One pile remaining
            if left == right:
                return piles[left]

            # Take left pile
            choose_left = piles[left] - dp(left + 1, right)

            # Take right pile
            choose_right = piles[right] - dp(left, right - 1)

            # Best possible score difference
            return max(choose_left, choose_right)

        # Alice wins if score difference is positive
        return dp(0, len(piles) - 1) > 0


# -----------------------------------------------------
# Example Usage
# -----------------------------------------------------

if __name__ == "__main__":

    s = Solution()

    print(s.stoneGame([5,3,4,5]))      # True
    print(s.stoneGame([3,7,2,3]))      # True



#or we can also return True directly because Alice always wins in this game with optimal play and even number of piles.


class Solution:
def stoneGame(self, piles: List[int]) -> bool:
    return True
    
