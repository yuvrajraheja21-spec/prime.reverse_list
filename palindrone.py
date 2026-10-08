n = int(input("Enter a number to check if it is palindrome: "))
#checking if the number is palindrome
str_n = str(n)
if str_n == str_n[::-1]:
    print(n, "is a palindrome.")
else:
    print(n, "is not a palindrome.")
