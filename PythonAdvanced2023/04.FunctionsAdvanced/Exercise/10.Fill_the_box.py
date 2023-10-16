def fill_the_box(height, length, width, *args):
    box_volume = height * length * width
    total_cubes_left = 0
    for cube in args:
        if isinstance(cube, int):
            if box_volume - cube >= 0:
                box_volume -= cube
            else:
                total_cubes_left += cube - box_volume
                box_volume = 0
        else:
            break

    if args[-1] != "Finish":
        total_cubes_left += sum(args[args.index("Finish") + 1:])

    if box_volume > 0:
        return f"There is free space in the box. You could put {box_volume} more cubes."
    else:
        return f"No more free space! You have {total_cubes_left} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
