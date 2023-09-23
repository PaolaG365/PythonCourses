number1, number2 = [int(x) for x in input().split()]

set1 = set()
set2 = set()

for el1 in range(number1):
    set1.add(int(input()))

for el2 in range(number2):
    set2.add(int(input()))

print(*set1.intersection(set2), sep='\n')
