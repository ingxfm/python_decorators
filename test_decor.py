from time import sleep

def delay_decorator(function):
    def wrapper_function():
        sleep(2)
        function()
        print('Ahoj!')
    return wrapper_function


@delay_decorator  # this is the so-called syntactic sugar. It substitutes the code in lines 21 and 22. 
def say_gym():
    print('gym!')

def say_damn():
    print('damn!')

say_gym()

# use this code below to call the function with the decorator without using syntactic sugar
# comment line 18 to use this version
decorated_function = delay_decorator(say_gym)
decorated_function()
