def my_func(x):
    if x==0:
        return 0
    else:
        return x+my_func(x-1)
print(my_func(5))