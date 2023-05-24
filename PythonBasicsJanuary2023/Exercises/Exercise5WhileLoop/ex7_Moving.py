volume_free_space = int(input()) * int(input()) * int(input())

while volume_free_space >= 0:
    packages = input()

    if packages == "Done" or (packages == "Done" and volume_free_space > 0):
        print(f'{volume_free_space} Cubic meters left.')
        break

    volume_free_space -= int(packages)

else:
    print(f'No more free space! You need {abs(volume_free_space)} Cubic meters more.')
