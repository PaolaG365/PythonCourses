lines = int(input())

unique_usernames = set()

for _ in range(lines):
    unique_usernames.add(input())

print(*unique_usernames, sep='\n')
