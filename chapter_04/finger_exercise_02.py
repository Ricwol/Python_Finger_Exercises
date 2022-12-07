# Finger exercise, p.93
# Write a function is_in that accepts two strings as arguments and returns True
# if either string occurs anywhere in the other, and False otherwise.
# Hint: you might want to use the built-in str operator in.

def is_in(string_1, string_2):
    """Returns True if either string occurs anywhere in the other."""
    string_match = False
    if (string_1 in string_2) or (string_2 in string_1):
        string_match = True
    return string_match


# Finger exercise, p.93
# Write a function to test is_in

def test_is_in(strings_1, strings_2):
    for string_1 in strings_1:
        for string_2 in strings_2:
            if is_in(string_1, string_2):
                print(f"Match found: {string_1!r} in {string_2!r}")
            else:
                print(f"No match:    {string_1!r} not in {string_2!r}")

strings_1 = ("aaabbbccc", "abcabcacbabc", "abbcccddddeeeee")
strings_2 = ("bc", "cacba", "eeeeeddddcccbbaaabbbccc")
test_is_in(strings_1, strings_2)
