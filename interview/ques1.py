def fun(s):
    if any(letter.isalnum() for letter in s):
        print("string has alphanumeric")
    if any(letter.isalpha() for letter in s):
        print("string has alpha")
    if any(letter.isdigit() for letter in s):
        print("string has digit")
    if any(letter.isupper() for letter in s):
        print("string has upper")
    if any(letter.islower() for letter in s):
        print("string has lower")

s=str(input("Enter String"))
fun(s)