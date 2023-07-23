first_symbol, second_symbol = input(), input()
string_to_search_in = input()
beginning_range = min(ord(first_symbol), ord(second_symbol))
end_range = max(ord(first_symbol), ord(second_symbol))
total_sum = 0

for char in string_to_search_in:
    if beginning_range < ord(char) < end_range:
        total_sum += ord(char)

print(total_sum)
