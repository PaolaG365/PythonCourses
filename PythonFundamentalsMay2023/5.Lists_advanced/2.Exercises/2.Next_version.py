version_program = input().split(".")
next_version = int("".join(version_program)) + 1
result = str(next_version)
print(*result, sep=".")
