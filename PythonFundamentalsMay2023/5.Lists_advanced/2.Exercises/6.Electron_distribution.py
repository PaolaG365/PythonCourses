def electron_distribution(number_electrons):
    shells = []
    number_shell = 1

    while number_electrons > 0:
        electrons_in_shell = 2 * (number_shell ** 2)
        number_shell += 1
        shells.append(electrons_in_shell) if electrons_in_shell < number_electrons else shells.append(number_electrons)
        number_electrons -= electrons_in_shell

    return shells


electrons_number = int(input())
print(electron_distribution(electrons_number))
