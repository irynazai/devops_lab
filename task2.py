
my_string = input('input string to check for palindrome: ').lower()

if not my_string:
    print("You input empty string! Try again.")
elif my_string == my_string[::-1]:
    print("It's palindrome.")
else:
    print("It's not palindrome.\n")
