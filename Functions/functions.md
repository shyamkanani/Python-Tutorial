## Functions

Functions are block of code. Once we define function we can call as many times as we want

#### Simple function
```python
def say_hello():
    print("Hello")
```

This is a simple function that print hello to output whenever we call the function by it's name

- In python functions are defined by **def** keyword followed by function name
- In python block is starts with colon(:) and follows four spaces visual indentation.
- To execute function we need to call it by it's name
- It's good to use snake_case(words separated by underscore(\_)) for function names

```python
say_hello()  # This line prints **Hello** message
```

#### Functions with arguments
We can pass arguments to functions for better usability

```python
def say_hello(times):
    print("Hello " * times)

say_hello(5)
```

- Here we are passing argument to work with output. Now the code prints **Hello** five times.
- Python don't add spaces at the end of strings, so we need to add them manually.
- The special syntax \*args in function definitions in python is used to pass a variable number of arguments to a function. It is used to pass a non-keyworded, variable-length argument list.
- The special syntax \*\*kwargs in function definitions in python is used to pass a keyworded, variable-length argument list. We use the name kwargs with the double star. The reason is because the double star allows us to pass through keyword arguments (and any number of them).

#### Return data using functions
Function can return data using return statement

```python
def sum(a , b):
    return a + b;

total = sum(10, 20)  # Returns 30
```

- Return statement return the execution to outside of function
- If execution encounters **return** statement in function, it stops execution there and exit function. Remaining line of code can't executed


#### Variable scopes (Local and global variables)
- Variables declared outside the function are global variables
- Variables declared within function are local variables
- Local variables take higher priority than global variables
- If we create variable within function it can't be accessed outside that function
- Global variables can accessed and modified by functions

```python
fun = "Fun"
def say_out():
    fun = "Not fun"
    return fun

say_out()  # output will be **Not fun**
```

##### data can't accessible outside function

```python
def say_out():
    fun = "Fun"
    return fun

say_out()  # Returns **Fun**
print(fun)  # This outputs **error**
```

#### Recursive function

- We can call the current function within the function

```python
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
```

- The comment below the function declaration is called Doc-string
- Writing doc-strings are helpful to explain the necessity of function and how is it going to work

#### Best practice

```python
def main():
    def say():
        print("Hello")

if __name__=="__main__":
    # The above line checks if the file is directly executing or imported by other file
    # If the file is imported the script within main function can't execute.
    # This only executes if the file is directly executed
    main()
```

- We can write function within function
- The top level function variables can be accessible and modified by lower-level functions
- If you write a single file script it is useful to use main function.

###### Author: Rayudubobbili
###### Date: 11-10-2018
