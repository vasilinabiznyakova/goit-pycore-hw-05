def caching_fibonacci():
    # Empty dictionary for cache
    cache = {}

    # Internal function for calculating Fibonacci numbers
    def fibonacci(n):
        if n in cache:
            return cache[n]
        else:
            if n <= 0:
                cache[n] = 0
            elif n == 1:
                cache[n] = 1
            else:
                cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

            print(cache)
            return cache[n]

    # Return the function with closure
    return fibonacci 

fib = caching_fibonacci()


assert fib(10) == 55
assert fib(15) == 610
assert fib(1) == 1
assert fib(-1) == 0
