# Each rucksack has two large compartments. All items of a given type are meant
# to go into exactly one of the two compartments.

# The list of items for each rucksack is given as characters all on a single line. 
# A given rucksack always has the same number of items in each of its two compartments, 
# so the first half of the characters represent items in the first compartment, 
# while the second half of the characters represent items in the second compartment.

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.

# Find the item type that appears in both compartments of each rucksack. 
# What is the sum of the priorities of those item types?
import string

def find_total_priority(file_path):
    first_rucksack = None
    second_rucksack = None

    priority_total = 0

    lower_case_priorities = dict()
    upper_case_priorities = dict()

    for idx, letter in enumerate(list(string.ascii_lowercase), start=1):
        lower_case_priorities[letter] = idx

    for idx, letter in enumerate(list(string.ascii_uppercase), start=27):
        upper_case_priorities[letter] = idx

    with open(file_path) as file:
        for line in file:
            half = len(line)//2
            first_rucksack = set(line[:half])
            second_rucksack = set(line[half:])

            shared_item = list(first_rucksack.intersection(second_rucksack))[0]
            
            if shared_item.islower():
                priority_total += lower_case_priorities[shared_item]
            else:
                priority_total += upper_case_priorities[shared_item]
    
    return priority_total

print(find_total_priority('input/day-3-input.txt'))


# --- Part Two ---

# For safety, the Elves are divided into groups of three. Every Elf carries a badge that 
# identifies their group. For efficiency, within each group of three Elves, the badge 
# is the only item type carried by all three Elves.

# Every set of three lines in your list corresponds to a single group, but each group 
# can have a different badge item type.

# Find the item type that corresponds to the badges of each three-Elf group. 
# What is the sum of the priorities of those item types?

def find_total_priority(file_path):
    elf_group = []
    first_elf = None
    second_elf = None
    third_elf = None

    lines = []

    priority_total = 0

    lower_case_priorities = dict()
    upper_case_priorities = dict()

    for idx, letter in enumerate(list(string.ascii_lowercase), start=1):
        lower_case_priorities[letter] = idx

    for idx, letter in enumerate(list(string.ascii_uppercase), start=27):
        upper_case_priorities[letter] = idx

    with open(file_path) as file:
        for line in file.readlines():
            lines.append(line.strip())
        
        while lines:
            first_elf = set(lines[0])
            second_elf = set(lines[1])
            third_elf = set(lines[2])

            shared_items = first_elf.intersection(second_elf)
            print(f'Shared items: {shared_items}')
            
            shared_badge = list(shared_items.intersection(third_elf))[0]
            print(f'Shared badge: {shared_badge}')

            if shared_badge.islower():
                priority_total += lower_case_priorities[shared_badge]
            else:
                priority_total += upper_case_priorities[shared_badge]


            if not lines:
                break
            
            del lines[:3]
            continue
    
    return priority_total

print(find_total_priority('input/day-3-input.txt'))