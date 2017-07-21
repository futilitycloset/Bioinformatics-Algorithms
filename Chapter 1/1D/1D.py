filename = 'rosalind_ba1d.txt'
f = open(filename, 'r')
dna_workfile = f.read()

pattern_and_dna = dna_workfile.split('\n')

dna_pattern = pattern_and_dna[0]
dna_sequence = pattern_and_dna[1]

pattern_length = len(dna_pattern)
sequence_length = len(dna_sequence)
pattern_count = 0
pattern_locations = []

difference_length = sequence_length - pattern_length

for i in range(difference_length):
	chunk = dna_sequence[i:i+pattern_length]
	if chunk == dna_pattern:
		pattern_count = pattern_count + 1
		pattern_locations.append(i)
	else:
		pass

print pattern_count
print(" ".join(str(x) for x in pattern_locations))