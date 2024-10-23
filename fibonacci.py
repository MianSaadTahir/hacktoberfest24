# Slightly Complex Python Program: Generate Fibonacci Sequence

def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Input from the user
num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))

# Check if the input is valid
if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    # Generate and print the Fibonacci sequence
    print(f"Fibonacci sequence up to {num_terms} terms: {fibonacci(num_terms)}")
