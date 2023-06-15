version_program = input().split(".")
next_version = int("".join(version_program)) + 1
result = str(next_version)
print(*result, sep=".")

# second version
# version_program = [int(x) for x in input().split(".")]
# version_program[-1] += 1
#
# for version in range(len(version_program) - 1, - 1, - 1):
#     if version_program[version] > 9 and version - 1 >= 0:
#         version_program[version] = 0
#         version_program[version - 1] += 1
#
# print(*version_program, sep=".")
