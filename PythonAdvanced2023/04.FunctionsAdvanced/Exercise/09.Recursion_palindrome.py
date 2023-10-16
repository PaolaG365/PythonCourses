def palindrome(word, index, result=''):
    index += 1
    result += word[-index]
    if index == len(word):
        return f"{word} is a palindrome" if result == word else f"{word} is not a palindrome"
    return palindrome(word, index, result)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
