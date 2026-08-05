"""
=========================================================
LeetCode 3310 - Remove Methods From Project
=========================================================

Problem
-------

There are n methods numbered from 0 to n-1.

You are given

n
k
invocations

where

[a, b]

means

Method a calls method b.

Method k contains a bug.

Therefore,

Method k

AND

every method reachable from k

are called

"SUSPICIOUS METHODS"

---------------------------------------------------------

Goal

Remove ALL suspicious methods.

BUT

Removal is allowed ONLY IF

no non-suspicious method calls
a suspicious method.

If any outside method calls a suspicious method,

nothing can be removed.

Return

Remaining methods after removal.

If removal isn't possible,

return every method.

=========================================================
Example 1
=========================================================

n = 4

k = 1

invocations

1 → 2

0 → 1

3 → 2

Picture

0 ----> 1 ----> 2
          ^
          |
3 --------|

Bug starts at

1

Suspicious

1

2

But

0 calls 1

3 calls 2

Both are NOT suspicious.

Therefore

Cannot remove.

Answer

[0,1,2,3]

=========================================================
Example 2
=========================================================

n = 5

k = 0

0 → 1

0 → 2

1 → 2

3 → 4

Picture

0
|\
| \
v  v
1→2

3→4

Bug starts

0

Suspicious

0

1

2

No outside method
calls

0

1

or

2

Safe to remove.

Remaining

3

4

Answer

[3,4]

=========================================================
Observation
=========================================================

Two separate tasks exist.

Task 1

Find every suspicious method.

Task 2

Check whether an outside method
calls any suspicious method.

=========================================================
Step 1
=========================================================

Construct graph.

Example

0 → 1

1 → 2

0 → 3

Adjacency List

0 : [1,3]

1 : [2]

2 : []

3 : []

=========================================================
Step 2
=========================================================

DFS from

k

Every visited node

becomes suspicious.

=========================================================
Example

Bug

1

Graph

1 →2→5

1→4

Visited

1

2

5

4

Suspicious

{1,2,4,5}

=========================================================
Step 3
=========================================================

Now check

Can they be removed?

For every edge

u → v

If

u is NOT suspicious

AND

v IS suspicious

Removal is impossible.

Return

0...

n-1

=========================================================
Why?
=========================================================

Suppose

0 →1→2

Bug

1

Suspicious

1

2

Method

0

is not suspicious.

If we remove

1

and

2

Method

0

will call a deleted method.

Project becomes invalid.

Hence

Nothing can be removed.

=========================================================
Otherwise
=========================================================

If every incoming edge
to suspicious methods

comes ONLY from suspicious methods,

remove them.

Return remaining methods.

=========================================================
Algorithm
=========================================================

Build graph

DFS from k

Mark suspicious nodes

Traverse every edge

If

outside → suspicious

Return all methods

Else

Return every non-suspicious method

=========================================================
Dry Run
=========================================================

n = 5

k = 0

Edges

0→1

0→2

1→2

3→4

---------------------------------

DFS

Visit

0

1

2

Suspicious

{0,1,2}

---------------------------------

Check edges

0→1

Inside

OK

0→2

Inside

OK

1→2

Inside

OK

3→4

Outside→Outside

OK

No invalid edge.

Return

[3,4]

=========================================================
Time Complexity
=========================================================

Building graph

O(E)

DFS

O(V+E)

Checking edges

O(E)

Overall

O(V+E)

=========================================================
Space Complexity
=========================================================

Graph

O(V+E)

Visited

O(V)

=========================================================
Python Solution
=========================================================
"""

from typing import List


class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:

        # Build directed graph
        graph = [[] for _ in range(n)]

        for u, v in invocations:
            graph[u].append(v)

        suspicious = [False] * n

        # DFS to mark suspicious methods
        def dfs(node):
            suspicious[node] = True
            for nei in graph[node]:
                if not suspicious[nei]:
                    dfs(nei)

        dfs(k)

        # Check if any outside method calls a suspicious method
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))

        # Remove suspicious methods
        return [i for i in range(n) if not suspicious[i]]


# -------------------------------------------------
# Example Usage
# -------------------------------------------------

if __name__ == "__main__":

    s = Solution()

    print(s.remainingMethods(
        4, 1,
        [[1,2],[0,1],[3,2]]
    ))
    # [0,1,2,3]

    print(s.remainingMethods(
        5, 0,
        [[1,2],[0,2],[0,1],[3,4]]
    ))
    # [3,4]

    print(s.remainingMethods(
        3, 2,
        [[1,2],[0,1],[2,0]]
    ))
    # []