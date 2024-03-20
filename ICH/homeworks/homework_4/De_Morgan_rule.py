# example
a = True
b = False
c = True
d = False

formula_1 = not ((a or b) and (c or d))
formula_2 = ((not a and not b) or (not c and not d))
is_equal = formula_1 is formula_2

print("Are the formulas equal? - ", is_equal)
