import sys

try:
	filename = raw_input('')
except:
	filename = ''
	
error = False
if filename == '':
	error = True
	filename = 'rosalind_ba1b.txt'
f = open(filename, 'r')
dna_workfile = f.read()

dna_and_pattern_list = dna_workfile.split('\n')

dna_sequence = dna_and_pattern_list[0]
dna_length = len(dna_sequence)
pattern_length = int(dna_and_pattern_list[1])
dna_difference = dna_length - pattern_length

def get_pattern(index, pattern_length = pattern_length, dna_sequence = dna_sequence):
	pattern = dna_sequence[index : index + pattern_length]
	return pattern 

def count_pattern(pattern, dna_sequence = dna_sequence):
	dna_difference = len(dna_sequence) - len(pattern)
	pattern_length = len(pattern)
	pattern_occurs = 0
	for i in range(dna_difference):
		chunk = dna_sequence[i:i+pattern_length]
		if chunk == pattern:
			pattern_occurs = pattern_occurs + 1
	return [pattern, pattern_occurs]

results = []

for i in range(dna_difference):
	new_pattern = get_pattern(i)
	pattern_already_exists = False
	for entry in results:
		if new_pattern == entry[0]:
			pattern_already_exists = True
	if pattern_already_exists == False:
		keep_pattern = count_pattern(new_pattern)
		results.append(keep_pattern)

biggest_number = 0
answer_list = []

for entry in results:
	if entry[1] > biggest_number:
		biggest_number = entry[1]

for entry in results:
	if entry[1] == biggest_number:
		answer_list.append(entry)

print answer_list

# biggest_number = max([x[1] for x in results])
# biggest_answers = [x for x in results if x[1] == biggest_number]
	
# one_more_list = [x[0] for x in biggest_answers]
# final_answer = ' '.join(one_more_list)

# big_answers = [['', 0]]

# for entry in results:
# 	print entry
# 	big_dummy = big_answers
# 	for other_entry in big_answers:
# 		if entry[1] == other_entry[1]:
# 			if entry[0] != other_entry[0]:
# 				big_dummy.append(entry)
# 		elif entry[1] > other_entry[1]:
# 			if entry[0] != other_entry[0]:
# 				big_dummy = [entry]
# 		else: 
# 			pass
# 			# entry[1] < other_entry[1]
# 	big_answers = big_dummy

# print big_answers
# print "end"

if error:
	print "ERROR TESTING RESULT ONLY"