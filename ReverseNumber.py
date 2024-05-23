def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    return reversed_num

# Test the function
input_number = int(input("Enter a number: "))
reversed_number = reverse_number(input_number)
print("Reversed number:", reversed_number)