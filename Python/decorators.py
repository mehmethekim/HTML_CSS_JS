def announce(f):
    def wrapper():
        print("Running the function...")
        f()
        print("End of the function...")
    return wrapper
def announce2(f):
    def wrapper():
        print("Running the function...")
        f(5)
        print("End of the function...")
    return wrapper
@announce
def hello():
    print("Hello World")
@announce2
def Number(x):
    print(x)
hello()

Number(5)