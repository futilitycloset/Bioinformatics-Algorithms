import collections

filename = 'rosalind_ba1e.txt'
f = open(filename, 'r')
dna_workfile = f.read()

genome_kLt = dna_workfile.split('\n')

genome = genome_kLt[0]

kLt = genome_kLt[1]

k_L_t = kLt.split(' ')

k_pattern_length = int(k_L_t[0])
L_window = int(k_L_t[1])
t_times = int(k_L_t[2])

genome_length = len(genome)
difference_length = genome_length - k_pattern_length
window_beginning = 0
current_start = 0
possible_patterns = {}
good_patterns = {}

initial_test_window = genome[window_beginning:(window_beginning+L_window)]
for i in range(int(len(initial_test_window)) - k_pattern_length + 1):
	new_pattern = initial_test_window[current_start:current_start+k_pattern_length]
	if new_pattern not in possible_patterns:
		possible_patterns[new_pattern] = 1
	if new_pattern in possible_patterns:
		possible_patterns[new_pattern] += 1
	for x in possible_patterns:
		if possible_patterns[x] >= t_times:
			if x not in good_patterns:	
				good_patterns[x] = 1
	current_start += 1

new_start = L_window - k_pattern_length + 1

for i in range(difference_length):
	advancing_pattern = genome[new_start:new_start + k_pattern_length]
	lost_pattern = genome[(new_start-k_pattern_length):(new_start-k_pattern_length)]
	if lost_pattern in possible_patterns:
		possible_patterns[lost_pattern] -= 1
	if advancing_pattern not in possible_patterns:
		possible_patterns[advancing_pattern] = 1
	if advancing_pattern in possible_patterns:
		possible_patterns[advancing_pattern] += 1
	for x in possible_patterns:
		if possible_patterns[x] >= t_times:
			if x not in good_patterns:	
				good_patterns[x] = 1
	new_start += 1

for key in good_patterns:
	print key

# for i in range(difference_length):
# 	all_current_patterns = []
# 	test_window = genome[window_beginning:(window_beginning+L_window)]
# 	test_length = len(test_window)
# 	for x in range(test_length):
# 		all_current_patterns.append(test_window[current_start:current_start + k_pattern_length])
# 		current_start += 1
# 	for x in all_current_patterns:
# 		if all_current_patterns.count(x) >= t_times:
# 			if x not in good_patterns:
# 				good_patterns.append(i)
# 			else: 
# 				pass
# 		else: 
# 			pass
# 	window_beginning += 1

# print good_patterns