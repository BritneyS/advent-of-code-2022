# This list represents the Calories of the food carried by elves
# (a different elf is carrying Calories after every line break).
#
# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

def find_max_calories_in_file(file_path):
    max = 0
    total = 0
    with open(file_path) as file:
        for line in file:
            if line.strip():
                total += int(line.strip())
            else:
                if total > max: max = total
                total = 0
                continue
    
    return max

print(find_max_calories_in_file('input/day-1-input.txt'))

# The Elves would instead like to know the total Calories carried by the
# top three Elves carrying the most Calories. That way, even if one of those
# Elves runs out of snacks, they still have two backups.

# Find the top three Elves carrying the most Calories. 
# How many Calories are those Elves carrying in total?

def find_top_three_largest_calories(file_path):
    first_highest = 0
    second_highest = 0
    third_highest = 0

    total = 0

    with open(file_path) as file:
        for line in file:
            if line.strip():
                total += int(line.strip())
            else:
                if total > first_highest: 
                    second_highest = first_highest
                    first_highest = total
                elif total > second_highest and total < first_highest: 
                    third_highest = second_highest
                    second_highest = total
                elif total > third_highest and total < second_highest:
                    third_highest = total

                total = 0
                continue

    return sum([first_highest, second_highest, third_highest])

print(find_top_three_largest_calories('input/day-1-input.txt'))