def fibonacci_generator(limit):
    a, b = 0, 1
    count = 0

    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

# Usage
fibonacci_limit = 10
fibonacci_gen = fibonacci_generator(fibonacci_limit)

for number in fibonacci_gen:
    print(number)



def generate_fibonacci_series(limit):
    series = []
    a, b = 0, 1

    while a <= limit:
        series.append(a)
        a, b = b, a + b

    return series

# Usage
limit = 10
fibonacci_series = generate_fibonacci_series(limit)
print(f"Fibonacci series up to {limit}: {fibonacci_series}")