start_symbol_ord = int(input())
end_symbol_ord = int(input())

for symbol in range(start_symbol_ord, end_symbol_ord + 1):
    print(chr(symbol), end=" ")
