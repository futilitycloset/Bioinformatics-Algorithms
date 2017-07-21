filename = 'rosalind_ba1h.txt'
f = open(filename, 'r')
dna_workfile = f.read()

first_split = dna_workfile.split('\n')
pattern = first_split[0]
genome = first_split[1]
allowed_errors = int(first_split[2])

genome_length = len(genome)
pattern_length = len(pattern)
start_point = 0
good_patterns = []

for i in range(genome_length - pattern_length):
	chunk = genome[start_point:start_point+pattern_length]
	error_counter = 0
	for x in range(0,len(chunk)):
		if chunk[x] != pattern[x]:
			error_counter += 1
		else:
			pass
	if error_counter <= allowed_errors:
		good_patterns.append(start_point)
	else:
		pass
	start_point += 1

print good_patterns