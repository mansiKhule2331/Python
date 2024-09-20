def cal(arr=[3]):
    arr.append(2)
    return arr
print(sum(cal())+sum(cal()))