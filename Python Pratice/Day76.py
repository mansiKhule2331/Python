x=10
def foo():
    global x
    x=20
foo()
print(x)