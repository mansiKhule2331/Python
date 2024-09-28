def my_function():
    try:
        print("Hello")
        return
    finally:
        print("world")
my_function()