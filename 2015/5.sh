#!/bin/bash
printf "Part 1: "; grep -P "(.*[aeiou]){3}" 5.txt | grep -P "(.)\1" | grep -Pv "(ab|cd|pq|xy)" | wc -l
printf "Part 2: "; grep -P "(..).*\1" 5.txt | grep -P "(.).\1" | wc -l
