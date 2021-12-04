with open("1.txt") as f:
    parens = f.read()


right, left = 0, 0
basement = -1
for i, paren in enumerate(parens):
    if paren == "(":
       left += 1
    elif paren == ")":
        right += 1
    total = left-right
    if total == -1 and basement == -1:
       basement = i + 1

print("Part 1:", left-right)
print("Part 2:", basement)
