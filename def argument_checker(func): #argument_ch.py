def argument_checker(func): #argument_checker関数
    def wrapper(*args, **kwargs): #
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError('Arguments must be integers')
        return func(*args, **kwargs)
    return wrapper

@argument_checker
def add_numbers(a, b):
    return a + b

print(add_numbers(1, 2))  # Output: 3
print(add_numbers(1, '2'))  # Raises TypeError