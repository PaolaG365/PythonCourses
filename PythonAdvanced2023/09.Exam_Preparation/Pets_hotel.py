from collections import defaultdict


def accommodate_new_pets(capacity: int, max_weight: float, *args: tuple[str, float]) -> str:
    pets_hotel = defaultdict(int)
    result = []

    # how are all pets accommodated is we have pets left out of the hotel?????? idk...
    for pet, weight in args:
        if capacity <= 0:
            result.append("You did not manage to accommodate all pets!")
            break
        if weight <= max_weight:
            pets_hotel[pet] += 1
            capacity -= 1
    else:
        result.append(f"All pets are accommodated! Available capacity: {capacity}.")

    result.append("Accommodated pets:")
    for type_pet, count in sorted(pets_hotel.items()):
        result.append(f"{type_pet}: {count}")

    return "\n".join(result)


print(
    accommodate_new_pets(
        10,
        15.0,
        ("cat", 5.8),
        ("dog", 10.0),
    )
)
print()
print(
    accommodate_new_pets(
        10,
        10.0,
        ("cat", 5.8),
        ("dog", 10.5),
        ("parrot", 0.8),
        ("cat", 3.1),
    )
)
print()
print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))
