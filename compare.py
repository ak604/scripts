a = [];
b = [];
with open('a.txt') as f:
    for line in f:
       a.append(line)
with open('b.txt') as f:
    for line in f:
       b.append(line)


for i in range(len(b)):
	present = False
	for j in range(len(a)):
		if b[i]==a[j]:
			present=True;
			break;
	if not present:
		print(b[i])
		
			
