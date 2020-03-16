data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
	avg = sum_len/len(data)
print(sum_len)
print('留言的平均長度為', avg)

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '比留言長度小於100')

good = []
for g in data:
	if 'good' in g:
		good.append(g)
print('一共有', len(good), '比留言有包含單詞Good')
print(good[162549])

wc = {}
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增key到字典

for word in wc:
	if wc[word] > 100:
		print(word,  wc[word])

print(len(wc))

while True:
	word = input('請輸入要查詢的文字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, "出現過", wc[word], '次')
	else:
		print('這個字沒有出現過喔')

print('感謝使用本查詢功能')
