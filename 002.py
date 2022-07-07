X = input('X = ')
Y = input('Y = ')
Z = input('Z = ')

left_part = not (X and Y and Z)
right_part = (not X) or (not Y) or (not Z)

print(left_part == right_part)