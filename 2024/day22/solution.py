from collections import defaultdict

MOD = 16777216


def evolve_secret(secret_number):
    secret_number ^= secret_number * 64
    secret_number %= MOD
    secret_number ^= secret_number // 32
    secret_number %= MOD
    secret_number ^= secret_number * 2048

    return secret_number % MOD


def solve(input_data):
    sum_of_all_final_secrets, diff_seq_to_price = 0, defaultdict(list)
    for initial_secret_number in input_data:
        diffs, seen_diff_sequences = [], set()
        for _ in range(2000):
            price = initial_secret_number % 10
            diffs.append({"price": price, "change_from_prev": price - diffs[-1]["price"] if len(diffs) > 0 else None})

            if len(diffs) > 4:
                diffs.pop(0)

            key = tuple([x["change_from_prev"] for x in diffs])
            if diffs[0]["change_from_prev"] is not None and tuple(key) not in seen_diff_sequences:
                diff_seq_to_price[key].append(price)
                seen_diff_sequences.add(key)

            initial_secret_number = evolve_secret(initial_secret_number)

        sum_of_all_final_secrets += initial_secret_number

    print("Part 1:", sum_of_all_final_secrets)
    print("Part 2:", sum(sorted(diff_seq_to_price.items(), key=lambda x: sum(x[1]), reverse=True)[0][1]))


if __name__ == "__main__":
    with open("input.txt") as f:
        input_data = [int(x) for x in f.read().split("\n")[:-1]]

    solve(input_data)
