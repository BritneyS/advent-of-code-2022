# --- Day 5: Supply Stacks ---
# The expedition can depart as soon as the final supplies have been unloaded from the ships. 
# Supplies are stored in stacks of marked crates, but because the needed supplies are buried 
# under many other crates, the crates need to be rearranged.

# The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of 
# the crates get crushed or fall over, the crane operator will rearrange them in a series of 
# carefully-planned steps. After the crates are rearranged, the desired crates will be at the 
# top of each stack.

# After the rearrangement procedure completes, what crate ends up on top of each stack? 
# (in a string, no spaces)

def find_top_crates(file_path):
    # Using a Python list as a LIFO stack for simplicity, with the last element as the first in the stack.
    # Setting these manually.
    crate_stacks = {
        '1': ['Z', 'J', 'N', 'W', 'P', 'S'],
        '2': ['G', 'S', 'T'],
        '3': ['V', 'Q', 'R', 'L', 'H'],
        '4': ['V', 'S', 'T', 'D'],
        '5': ['Q', 'Z', 'T', 'D', 'B', 'M', 'J'],
        '6': ['M', 'W', 'T', 'J', 'D', 'C', 'Z', 'L'],
        '7': ['L', 'P', 'M', 'W', 'G', 'T', 'J'],
        '8': ['N', 'G', 'M', 'T', 'B', 'F', 'Q', 'H'],
        '9': ['R', 'D', 'G', 'C', 'P', 'B', 'Q', 'W']
    }

    with open(file_path) as file:
        lines = file.readlines()
        del lines[:10]

        for line in lines:
            _, number_of_crates_to_move, _, from_stack, _, to_stack = line.strip().split(' ')

            if not " " in from_stack and not " " in to_stack: crate_stacks = move_crates_in_stack(crate_stacks, int(number_of_crates_to_move), from_stack, to_stack)

        top_crates_of_stacks = list(map(lambda stack: crate_stacks[stack][-1] if crate_stacks[stack] else ' ', crate_stacks))
    
    return ''.join(top_crates_of_stacks)

def move_crates_in_stack(stack, num_of_crates, from_stack, to_stack):
    for _ in range(num_of_crates):
        if stack[from_stack]:
            moved_crate = stack[from_stack].pop()
            stack[to_stack].append(moved_crate)
    return stack

print(find_top_crates('input/day-5-input.txt'))

# --- Part Two ---

# The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, 
# an extra cup holder, and the ability to pick up and move multiple crates at once.

# The crates maintain their order when moved.

# After the rearrangement procedure completes, what crate ends up on top of each stack?

def find_top_crates(file_path):
    # Using a Python list as a LIFO stack for simplicity, with the last element as the first in the stack.
    # Setting these manually.
    crate_stacks = {
        '1': ['Z', 'J', 'N', 'W', 'P', 'S'],
        '2': ['G', 'S', 'T'],
        '3': ['V', 'Q', 'R', 'L', 'H'],
        '4': ['V', 'S', 'T', 'D'],
        '5': ['Q', 'Z', 'T', 'D', 'B', 'M', 'J'],
        '6': ['M', 'W', 'T', 'J', 'D', 'C', 'Z', 'L'],
        '7': ['L', 'P', 'M', 'W', 'G', 'T', 'J'],
        '8': ['N', 'G', 'M', 'T', 'B', 'F', 'Q', 'H'],
        '9': ['R', 'D', 'G', 'C', 'P', 'B', 'Q', 'W']
    }

    with open(file_path) as file:
        lines = file.readlines()
        del lines[:10]

        for line in lines:
            _, number_of_crates_to_move, _, from_stack, _, to_stack = line.strip().split(' ')

            if not " " in from_stack and not " " in to_stack: crate_stacks = move_crates_in_stack(crate_stacks, int(number_of_crates_to_move), from_stack, to_stack)

        top_crates_of_stacks = list(map(lambda stack: crate_stacks[stack][-1] if crate_stacks[stack] else ' ', crate_stacks))
    
    return ''.join(top_crates_of_stacks)

def move_crates_in_stack(stack, num_of_crates, from_stack, to_stack):
    crane_stack = []

    for _ in range(num_of_crates):
        if stack[from_stack]:
            moved_crate = stack[from_stack].pop()
            crane_stack.append(moved_crate)
            
    crane_stack.reverse()
    stack[to_stack] = stack[to_stack] + crane_stack

    return stack

print(find_top_crates('input/day-5-input.txt'))

