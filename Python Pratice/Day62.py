a={1:'one',2:'two',3:'three'}
b={k: v for k,v in a.items() if k%2==0}
print(b)