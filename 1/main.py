input = open('input.txt').read().split('\n\n')

totals = []

for group in input:
    total = 0
    for num in group.split('\n'):
        total = total + int(num)
    totals.append(total)

print(totals)
print('\nSorted:')
totals.sort(reverse=True)
print(totals[0]+totals[1]+totals[2])