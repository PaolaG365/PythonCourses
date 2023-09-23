lines = int(input())

unique_compounds = set()

for line in range(lines):
    compounds = input().split()
    unique_compounds.update(compounds)

print(*unique_compounds, sep='\n')
