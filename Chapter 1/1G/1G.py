filename = 'rosalind_ba1g.txt'
f = open(filename, 'r')
dna_workfile = f.read()

genome_length = len(dna_workfile)
half = genome_length/2
string_one = dna_workfile[0:half-1]
string_two = dna_workfile[half:genome_length]
difference_count = 0

for i in range(0, half-1):
	if string_one[i] != string_two[i]:
		difference_count += 1

print difference_count