# --- Day 1: Trebuchet?! ---
# 
# Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.
# 
# You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.
# 
# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
# 
# You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").
# 
# As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.
# 
# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
# 
# For example:
# 
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# 
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.
# 
# Consider your entire calibration document. What is the sum of all of the calibration values?
# 
import os

path = os.path.dirname(os.path.realpath(__file__))

with open(f"{path}/day_01_input.txt") as file:
    lines = [line.rstrip() for line in file]

print("part1")
total = 0

for line in lines:
    number = ""
    for char in line:
        if char.isdigit():
            number += char
            break
    for char in reversed(line):
        if char.isdigit():
            number += char
            break
    total += int(number)
print(total)

#--- Part Two ---
#
#Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".
#
#Equipped with this new information, you now need to find the real first and last digit on each line. For example:
#
#two1nine
#eightwothree
#abcone2threexyz
#xtwone3four
#4nineeightseven2
#zoneight234
#7pqrstsixteen
#
#In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.
#
#What is the sum of all of the calibration values?

print("part2")
total = 0

numbers_str = (
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
)

for line in lines:
    number = ""

    low_index = 99
    low_index_char = ""
    high_index = 0
    high_index_char = ""

    i = 0
    for number_str in numbers_str:
        i += 1

        low_idx = line.find(number_str)
        if low_idx == -1:
            continue

        high_idx = low_idx + len(number_str) -1
        j = 1
        while (line[high_idx+1:].find(number_str) != -1):
            j += 1
            high_idx = line[high_idx:-1].find(number_str) + j * len(number_str) -1

        if (low_idx < low_index):
            low_index = low_idx
            low_index_char = str(i)
        if (high_idx > high_index):
            high_index = high_idx
            high_index_char = str(i) 

    c = 0
    for char in line:
        if c > low_index:
            break
        if char.isdigit():
            low_index_char = char
            break
        c += 1    

    c = len(line) - 1
    for char in reversed(line):
        if c < high_index:
            break
        if char.isdigit():
            high_index_char = char
            break
        c -= 1    

    number = low_index_char + high_index_char
    total += int(number)
print(total)

