def my_function():
    x=10
    def inner_function():
        nonlocal x
        x+=5
    inner_function()
    print(x)
my_function()