def foo():
    try:
        print(1,end=' ')
    finally:
        print(2)
k=foo()
print(k)