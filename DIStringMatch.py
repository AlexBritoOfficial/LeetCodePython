"""
A permutation perm of n + 1 integers of all the integers in the range [0, n],
 can be represented as a string s of length n where:

s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it.
If there are multiple valid permutations perm, return any of them.

perm = [0,1,2,3,4]

p1 = 0, will be set to 0
p2 = 4, will be set to the length of s

Example 1:

Pseudo Code:
Given the Input: s = "IDID"

1)  Create a for loop with a range of the length of the input s,
    iterate through the characters of string s, do two checks

    Check 1)  if s[i] == 'I"

        if this is true, we will append p1 to perm to the list

        -> [0]

        increment p1, after we insert p1 into the list

    Check 2)  elif s[i] == 'D':

        if this is true, we will append p2 to perm to the list

        -> [0,4]

        decrement p2

2) Once we exit the for loop, we append p1 to the perm list.

3) Return perm
"""

def diStringMatch(s):
    """
    :type s: str
    :rtype: List[int]
    """

    p1 = 0
    p2 = len(s)
    perm = list()

    for i in range(len(s)):

        if s[i] == "I":
            perm.append(p1)
            p1 += 1

        elif s[i] == "D":
            perm.append(p2)
            p2 -= 1

    return perm.append(p1)

if __name__ == "__main__":

    s = "IDID"

    diStringMatch(s)