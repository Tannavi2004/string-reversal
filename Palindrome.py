def is_pal(s):
    s = s.lower().replace(" ", "")
    return "Palindrome" if s == s[::-1] else "Not a palindrome"

print(is_pal(input("Enter text: ")))
