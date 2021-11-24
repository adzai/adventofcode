#include <stdio.h>

int part1(int input) {
    for (int i = 650000; i < input; i++) {
        int sum = 0;
        for (int j = 1; j < i/2 + 1; j++) {
            if (i % j == 0) {
                sum += j * 10;
            }
        }
        sum += i * 10;
        if (sum >= input) {
            return i;
        }
    }
}

int part2(int input) {
    for (int i = 700000; i < input; i++) {
        int sum = 0;
        for (int j = 1; j < i/2 + 1; j++) {
            if (j * 50 < i) {
                continue;
            }
            else if (i % j == 0) {
                sum += j * 11;
            }
        }
        sum += i * 11;
        if (sum >= input) {
            return i;
        }
    }
}

int main(void) {
    int input = 29000000;
    printf("Part 1: %d\n", part1(input));
    printf("Part 2: %d", part2(input));
    return 0;
}


