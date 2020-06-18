a=True

b=False
print(not a or b)
print((a or b) and not (a and b))
print((a and b) or not (a or b))
print((a and not b) or (not a and b))
print((a and not b))