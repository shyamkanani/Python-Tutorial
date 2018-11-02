# Author: Rayudubobbili
# Date: 11-10-2018

"""
    There is no main function in Python like other language, C, C++.
    So main() function is no special in Python, it works same as
    other functions. It doesn't gets called directly, automatically
    when program loads, like other language. It only gets executed
    if program call the function.

    For simple program, let's assume function name "main" but
    you can name it anything, as we discussed above, there is no
    main function in Python.
"""

"""
    How to write function in Python?

    def function_name(function_argument_names_if_any):
        function_body

    where,
    'def' is a keyword for function.
    'function_name' is name of function, you can write any name of function.
    'functions_argument_names_if_any' are functions arguments, if function has any.
    You don't have to write argument type, only name is enough.
    'function_body' is body of the function, where logic of function goes.
    It includes for/while loop, if conditional statement, print statement etc.
    according to function logic.

    Example:

    def print_my_name(my_name):
        print(my_name)


    Here, as you can see 'print_my_name' is a function name.
    'my_name' is argument name. Note that in python, we don't need to declare
    argument type.
    'print(my_name)' is function body, which will print name pass to function.

    As you can observe, that in Python, we neither declare function return type
    nor argument type.

"""

# Following are examples of different types of functions with different no of
# arguments.
# Main function
def main():

    # Simple function
    def say_hello():
        print("Hello")

    # calling function
    print(say_hello())

    # Function with arguments
    def say_hello_with_argument(times):
        print("Hello " * times)

    print(say_hello_with_argument(10))

    # Function with return data
    def sum(a, b):
        return a + b

    count = sum(1, 4)

    # local variable take highest priority, and function can handle global variables
    fun = "Fun"
    def mood():
        fun = "Not fun"
        return fun

    print(mood())

    # Local variable cant be accessed out side

    def say_out():
        word = "Fun"
        return word

    print(say_out())
    # print(word)  # raise error

    # Recursive function
    def fibonacci(n):
        '''Recursive function to find the fibonacci number of given number
        using f(n-1) + f(n-2) formula
        '''
        if n <= 1:
            return n
        else:
            return(fibonacci(n-1) + fibonacci(n-2))

    for i in range(10):
        print(fibonacci(i))
"""
    __name__ is variable which returns name of the current module.
    If module is running directly as a source/main program it will
    return '__main__'.
    If module is imported to other program or module called 'xyz.py'
    then __name__ will return 'xyz.py' -- name of imported module.

    More detail: https://stackoverflow.com/questions/419163/what-does-if-name-main-do
"""
if __name__=='__main__':
    main()
