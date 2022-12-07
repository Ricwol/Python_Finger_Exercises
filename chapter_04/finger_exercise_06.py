# Finger exercise, p.110
# What does s.find(sub) return if sub does not occur in s?
#
# Checking the docs tells us that s.find(sub) will return -1 if sub not in s
# find(...)
#    Return the lowest index in S where substring sub is found,
#    such that sub is contained within S[start:end].  Optional
#    arguments start and end are interpreted as in slice notation.
#
#    Return -1 on failure.


# Finger exercise:
# Use find to implement a function satisfying the specification

def find_last(s, sub):
    """s and sub are non-empty strings
       Returns the index of the last occurrence of sub in s.
       Returns None if sub does not occur in s
    """
    if sub not in s:
        return None
    last = -1
    start = 0
    while start >= 0:
        start = s.find(sub, start+1)
        last = max(start, last)
    return last
