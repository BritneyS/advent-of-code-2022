# --- Day 4: Camp Cleanup ---
# Space needs to be cleared before the last supplies can be unloaded from the ships, 
# and so several Elves have been assigned the job of cleaning up sections of the camp. 
# Every section has a unique ID number, and each Elf is assigned a range of section IDs.

# However, as some of the Elves compare their section assignments with each other, 
# they've noticed that many of the assignments overlap. To try to quickly find overlaps 
# and reduce duplicated effort, the Elves pair up and make a big list of the section 
# assignments for each pair (your puzzle input).

# Some of the pairs have noticed that one of their assignments fully contains the other. 
# For example, 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6. In pairs where 
# one assignment fully contains the other, one Elf in the pair would be exclusively 
# cleaning sections their partner will already be cleaning, so these seem like the most 
# in need of reconsideration.

# In how many assignment pairs does one range fully contain the other?

def find_overlapping_ranges(file_path):
    overlap_count = 0

    with open(file_path) as file:
        for line in file:
            range1, range2 = line.split(',')
            range1_start, range1_stop = range1.split('-')
            range2_start, range2_stop = range2.split('-')

            range_set_A = set(range(int(range1_start), int(range1_stop)+1))
            range_set_B = set(range(int(range2_start), int(range2_stop)+1))

            if range_set_A.intersection(range_set_B) == range_set_A or range_set_A.intersection(range_set_B) == range_set_B:
                overlap_count += 1
            
    return overlap_count


print(find_overlapping_ranges('input/day-4-input.txt'))

# --- Part Two ---
# It seems like there is still quite a bit of duplicate work planned. 
# Instead, the Elves would like to know the number of pairs that overlap at all.

# In how many assignment pairs do the ranges overlap?

def find_overlapping_ranges(file_path):
    overlap_count = 0

    with open(file_path) as file:
        for line in file:
            range1, range2 = line.split(',')
            range1_start, range1_stop = range1.split('-')
            range2_start, range2_stop = range2.split('-')

            range_set_A = set(range(int(range1_start), int(range1_stop)+1))
            range_set_B = set(range(int(range2_start), int(range2_stop)+1))

            if range_set_A.intersection(range_set_B):
                overlap_count += 1
            
    return overlap_count


print(find_overlapping_ranges('input/day-4-input.txt'))