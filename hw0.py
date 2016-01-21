file = open('iowa-liquor-sample.csv', 'r')
count = 0
key = "single malt scotch"

for line in file:
	lowercase = line.lower()
	if lowercase.find(key) != -1:
		count += 1

print count