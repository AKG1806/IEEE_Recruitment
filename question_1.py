stairs = range(1, 7)
for steps in stairs:
    gaps = 6 - steps
    print(" " * gaps + "*" * steps)