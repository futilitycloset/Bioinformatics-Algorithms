try:
	filename = raw_input('Tell me your filename: ')
except:
	filename = ''

error = False
if filename == '':
	error = True
	filename = 'rosalind_ba1a.txt'
f = open(filename, 'r')
dna_workfile = f.read()

print dna_workfile
print type(dna_workfile)
dna_and_pattern_list = dna_workfile.split('\n')
print dna_and_pattern_list

dna_sequence = dna_and_pattern_list[0]
pattern = dna_and_pattern_list[1]
dna_length = len(dna_sequence)
pattern_length = len(pattern)
pattern_occurs = 0

print dna_length, pattern_length

dna_difference = dna_length - pattern_length

for i in range(dna_difference):
	chunk = dna_sequence[i:i+pattern_length]
	if chunk == pattern:
		pattern_occurs = pattern_occurs + 1

print pattern_occurs
if error:
	print "ERROR TESTING RESULT ONLY"