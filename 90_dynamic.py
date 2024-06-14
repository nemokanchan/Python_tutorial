def fibonacci(n):
    fib = [0, 1]  # Initialize the list with the first two Fibonacci numbers
    
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])  # Calculate the next Fibonacci number
        
    return fib[n]

# Test the function
number = int(input("Enter the number to find its Fibonacci series: "))
print("Fibonacci series of", number, "is:", fibonacci(number))
