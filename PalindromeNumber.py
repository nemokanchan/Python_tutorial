def is_palindrome(num):
    # Convert the number to a string for easy comparison
    num_str = str(num)
    # Compare the string with its reverse
    return num_str == num_str[::-1]

# Test the function
input_number = int(input("Enter a number: "))
if is_palindrome(input_number):
    print("The number is a palindrome!")
else:
    print("The number is not a palindrome.")