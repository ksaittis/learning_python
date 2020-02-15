def say_hello(function):
    def new_function():
        print("Hello, world!")
        function()

    return new_function


@say_hello
def myfunc():
    print("This is my function.")


@say_hello
def mysecondfunc():
    print("This is my second function.")


if __name__ == '__main__':
    myfunc()
    mysecondfunc()
