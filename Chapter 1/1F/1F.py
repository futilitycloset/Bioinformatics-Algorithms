filename = 'rosalind_ba1f.txt'
f = open(filename, 'r')
genome = f.read()

G_count = 0
C_count = 0
low_skew = 0
low_skews = {}

for x in range(len(genome)):
	nuc = genome[x]
	if nuc == "G" or "C":
		if nuc == "G":
			G_count += 1
		if nuc == "C":
			C_count += 1
		current_skew = G_count - C_count
		print current_skew
		if current_skew <= low_skew:
			low_skew = current_skew
			low_skews[x] = low_skew

print low_skews

lowest = min(low_skews.values())
print int(lowest)

min_keys = [k for k in low_skews if low_skews[k] == lowest]
print min_keys

# add one to account for indexing

# for x in range(genome_length):
# 	nuc = genome[current_place]
# 	place = genome.index(nuc)
# 	if nuc == "G":
# 		G_count += 1
# 	if nuc == "C":
# 		C_count += 1
# 	current_skew = G_count - C_count
# 	if current_skew <= low_skew:
# 		low_skew_locations.append(x)
# 		low_skew = current_skew
# 		low_skew_counts.append(low_skew)
# 		for i in low_skew_locations:
# 			list_place = low_skew_locations.index(i)
# 			if i > low_skew:
# 				low_skew_locations.pop(i)
# 				low_skew_counts.pop(i)
# 	current_place += 1

# print low_skews