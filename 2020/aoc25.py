card_pub = 5764801
door_pub = 17807724
card_pub = 17607508
door_pub = 15065270

target = 1
card_loop = 0
while target != card_pub:
    target *= 7
    target %= 20201227
    card_loop += 1

door_loop = 0
target = 1
while target != door_pub:
    target *= 7
    target %= 20201227
    door_loop += 1

print(card_loop, door_loop)


card_sec = 1
for _ in range(card_loop):
    card_sec *= door_pub
    card_sec %= 20201227

print(card_sec)
