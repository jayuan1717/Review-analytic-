data = []
with open('review.txt', 'r') as f:
	for line in f:
		data.append(line)
print(len(data))