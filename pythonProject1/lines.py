genome = 'ATGG'
i = 1
print(genome[i])

genome = 'ATGG'
for i in range(4):
    print(genome[i])

genome = 'ATTG'
for c in genome:
    print(c)

genome = input()
cnt = 0
for nucl in genome:
    if nucl == 'C':
        cnt += 1
print(cnt)

genome = input()
print(genome.count('C'))