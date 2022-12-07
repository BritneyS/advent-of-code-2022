# --- Day 6: Tuning Trouble ---

# To fix the communication system, you need to add a subroutine to the device 
# that detects a start-of-packet marker in the datastream. In the protocol being 
# used by the Elves, the start of a packet is indicated by a sequence of four 
# characters that are all different.

# How many characters need to be processed before the first start-of-packet marker is detected?

def find_packet_start(file_path):
    comparison = []
    start_of_packet_marker = 0

    with open(file_path) as file:
        line = file.readline()

        for idx, letter in enumerate(line, start=1):
            while len(comparison) < 4:
                comparison.append(letter)

            if len(set(comparison)) == 4:
                start_of_packet_marker = idx
                break

            comparison.pop(0)
        
    return start_of_packet_marker

print(find_packet_start('input/day-6-input.txt'))

# --- Part Two ---

# A start-of-message marker is just like a start-of-packet marker, except it consists 
# of 14 distinct characters rather than 4.

# How many characters need to be processed before the first start-of-message marker is detected?

def find_packet_start(file_path):
    comparison = []
    start_of_packet_marker = 0

    with open(file_path) as file:
        line = file.readline()

        for idx, letter in enumerate(line, start=1):
            while len(comparison) < 14:
                comparison.append(letter)

            if len(set(comparison)) == 14:
                start_of_packet_marker = idx
                break

            comparison.pop(0)
        
    return start_of_packet_marker

print(find_packet_start('input/day-6-input.txt'))


            
            