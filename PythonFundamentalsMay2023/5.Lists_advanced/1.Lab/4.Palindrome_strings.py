def searched_palindrome(user_string, palindrome_to_be_found):

    palindromes_in_list = [word for word in user_string if word == word[::-1]]
    count_searched_palindrome = palindromes_in_list.count(palindrome_to_be_found)
    result = f"\nFound palindrome {count_searched_palindrome} times"

    return palindromes_in_list, result


string_user = input().split()
palindrome = input()
print(*searched_palindrome(string_user, palindrome))
