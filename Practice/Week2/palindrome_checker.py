def checkPalindrome(s: str):
    s = s.lower()
    clean_word = ''.join(filter(str.isalpha, s))
    return clean_word == clean_word[::-1]

print(checkPalindrome(" Abb&&& a "))
