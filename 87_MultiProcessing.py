import multiprocessing

def square(n):
    return n * n

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    # Create a Pool of processes
    with multiprocessing.Pool() as pool:
        # Apply the function 'square' to each number in 'numbers' using parallel processing
        results = pool.map(square, numbers)

    print("Original numbers:", numbers)
    print("Squared numbers:", results)