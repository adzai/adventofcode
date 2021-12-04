import ast
import re

memory_count = 0
raw_count = 0

with open("8.txt") as f:
    lines = f.readlines()
ctr = 0
for line in lines:
    raw = line.strip()
    parsed = ast.literal_eval(raw)  # This is probably cheating

    raw_count += len(raw)
    memory_count += len(parsed)
    ctr += 1

print(raw_count - memory_count)

raw_count = 0
encoded_count = 0

for line in lines:
    raw = line.strip()
    encoded = re.sub(r'(["\\])', r'\\\1', raw)

    raw_count += len(raw)
    encoded_count += len(encoded) + 2  # Quotes are not included

print(encoded_count - raw_count)
