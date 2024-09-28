def ispalindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]
text = input("Enter a word or sentence: ")
if ispalindrome(text):
    print(f"{text} is a palindrome.")
else:
    print(f" {text} ia not a palindrome")