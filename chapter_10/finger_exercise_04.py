# Finger exercise, p.219
# What is the value of the following expression?

exp = "isinstance(\"ab\", str) == isinstance(str, str)"

# "ab" is of type str
print("type(\"ab\") =", type("ab"))

# So the left side of the comparison operator evaluates to True
print("\"ab\" is of type str is", isinstance("ab", str))

# str is a class and therefore of type 'type'
print("type(str) =", type(str))

# This means isinstance will return False
print("str is of type str is", isinstance(str, str))

# Thus the expression will evaluate to False, as True == False is False
print(exp, "is", isinstance("ab", str) == isinstance(str, str))

# To get type str we have to call the class
# This will return True
print("isinstance(str(), str) is", isinstance(str(), str))
