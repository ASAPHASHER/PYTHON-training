text = input("Enter text: ")
print("Palindrome" if text == text[::-1] else "Not Palindrome")