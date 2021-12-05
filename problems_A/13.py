friends, bottles, ml, limes, dolki, salt, fr_ml, fr_salt = map(int, input().split())

ml = ml * bottles
limes = dolki * limes

fr_ml = ml // (friends * fr_ml)
fr_salt = salt // (friends * fr_salt)

print(min(fr_ml, fr_salt, limes//friends))