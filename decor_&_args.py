def logging_decorator(function):
    def wrapper_logging(*args, **kwargs):
        result = function(args[0], args[1], args[2])
        print(f'You called a function: {function.__name__}{args}.')
        print(f'It return: {result}.')
    return wrapper_logging



@logging_decorator
def add_numbers(n1, n2, n3):
    return n1 + n2 +n3

add_numbers(1, 2, 6)
