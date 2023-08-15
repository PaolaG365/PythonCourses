##################################
# 1. Rectangle 10 * 10(without spaces)

k = 10
for row in range(10):
    print("*" * k)


##################################
# 2. Rectangle of n * n stars
'''
****
****
****
****
'''

k = int(input())
for row in range(k):
    print("*" * k)


##################################
# 3. Square of Stars
'''
* * *
* * *
* * *
'''

k = int(input())
for row in range(k):
    for col in range(k):
        print("* ", end="")
    print()


##################################
# 4. Triangle of Dollars
'''
$
$ $
$ $ $
$ $ $ $
'''

k = int(input())
for row in range(1, k + 1):
    print("$ " * row)


##################################
# 5. Square Frame
'''
+ - - +
| - - |
| - - |
+ - - +
'''

k = int(input())
for row in range(1, k + 1):
    for col in range(1, k + 1):
        if (row == 1 and col == 1) or (row == k and col == k) or (row == k and col == 1)\
                or (row == 1 and col == k):
            print("+ ", end="")
        elif col == 1 or col == k:
            print("| ", end="")
        else:
            print("- ", end="")
    print()

# Variant 2
# k = int(input())
# for row in range(1, k + 1):
#     if row == 1 or row == k:
#         print("+ ", "- " * (k - 2), "+", sep="")
#     else:
#         print("| ", "- " * (k - 2), "|", sep="")


##################################
# 6. Rhombus of Stars/Diamond of stars
'''
  *
 * *
* * *
 * *
  *
'''

k = int(input())
for row in range(1, k + 1):
    print(" " * (k - row), "*", " *" * (row - 1), sep="")

k -= 1
for second_rows in range(k - 1, -1, -1):
    print(" " * (k - second_rows), "*", " *" * second_rows, sep="")


################################
# 7. Christmas Tree
'''
    |
  * | *
 ** | **
*** | ***
'''

k = int(input())
tree_space = k
for left_side in range(k + 1):
    print(" " * tree_space, "*" * left_side, " | ", sep="", end="")
    print("*" * left_side, end="")
    print()
    tree_space -= 1


################################
# 8. Sunglasses shape
'''
********    ********
*//////*||||*//////*
*//////*    *//////*
********    ********
'''

k = int(input())
for sunglasses_form in range(k):
    if sunglasses_form == 0 or sunglasses_form == k - 1:
        print("*" * (k * 2), " " * k, "*" * (k * 2), sep="")
    elif sunglasses_form == (k - 1) // 2:
        print("*", "/" * (k * 2 - 2), "*", "|" * k, "*", "/" * (k * 2 - 2), "*", sep="")
    else:
        print("*", "/" * (k * 2 - 2), "*", " " * k, "*", "/" * (k * 2 - 2), "*", sep="")


################################
# 9. House shape
'''
--*--
-***-
*****
|***|
|***|
'''

k = int(input())
house_roof = (k + 1) // 2
roof_stars = 0
if k % 2 == 0:
    roof_stars = 2
else:
    roof_stars = 1
roof_lines = (k - roof_stars) // 2

for house_form in range(k):
    if house_form < house_roof:
        print("-" * roof_lines, "*" * roof_stars, "-" * roof_lines, sep="")
        roof_stars += 2
        roof_lines -= 1
    else:
        print("|", "*" * (k - 2), "|", sep="")


################################
# 10. Diamond shape
'''
---**---
--*--*--
-*----*-
*------*
-*----*-
--*--*--
---**---
'''

k = int(input())
side_symbols = (k - 1) // 2
mid_symbols = k - (2 * side_symbols) - 2
form_mid = (k + 1) // 2

for j in range(form_mid):
    print("-" * side_symbols, "*", "-" * mid_symbols,
          f"*" if mid_symbols >= 0 else "", "-" * side_symbols, sep="")
    side_symbols -= 1
    mid_symbols += 2

side_symbols += 2  # resets counters for next iteration
mid_symbols -= 4

for n in range(form_mid - 1):
    print("-" * side_symbols, "*", "-" * mid_symbols,
          "*" if mid_symbols >= 0 else "", "-" * side_symbols, sep="")
    side_symbols += 1
    mid_symbols -= 2
