def func(a,b=2,*args,**kwargs):
    print(a,b,args,kwargs)
func(1,3,4,5,c=6,d=7)