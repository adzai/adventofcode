from collections import defaultdict
from typing import Counter


def get_letters_sector_id_and_checksum(entry: str) -> tuple[list[str], int, str]:
    first_part, checksum = entry.split("[")
    checksum = checksum.replace("]", "")
    s = first_part.split("-")
    sector_id = s[-1]
    letters = []
    for val in s[:-1]:
        letters.extend(list(val))

    return letters, int(sector_id), checksum


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read().split("\n")[:-1]

    sector_id_sum = 0
    for entry in input:
        letters, sector_id, checksum = get_letters_sector_id_and_checksum(entry)

        buckets = defaultdict(list)
        most_common = Counter(letters).most_common()
        for x, y in most_common:
            buckets[y].append(x)

        most_common_sorted_alphabetically = []
        for y in sorted(buckets.keys(), reverse=True):
            most_common_sorted_alphabetically.extend(sorted(buckets[y]))

            if len(most_common_sorted_alphabetically) >= 5:
                break

        if checksum == "".join(most_common_sorted_alphabetically[:5]):
            sector_id_sum += sector_id

    print("Part 1:", sector_id_sum)

    for entry in input:
        letters_to_decrypt = entry.split("-")[:-1]
        sector_id = entry.split("-")[-1].split("[")[0]
        rot_num = int(sector_id) % 26
        new_letters = []
        for letter in letters_to_decrypt:
            for char in letter:
                new_letters.append(chr((((ord(char) - 97) + rot_num) % 26) + 97))

            new_letters.append(" ")

        decrypted = "".join(new_letters)
        if "northpole object storage" in decrypted:
            print("Part 2:", sector_id)
            break
