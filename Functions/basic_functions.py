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
