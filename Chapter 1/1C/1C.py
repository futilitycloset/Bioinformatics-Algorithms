filename = 'rosalind_ba1c.txt'
f = open(filename, 'r')
dna_workfile = f.read()

sequence_length = len(dna_workfile)

reverse_complement = ''

for i in dna_workfile:
	if i == 'A':
		reverse_complement += 'T'
	elif i == 'T':
		reverse_complement += 'A'
	elif i == 'C':
		reverse_complement += 'G'
	elif i == 'G':
		reverse_complement += 'C'

print reverse_complement[::-1]