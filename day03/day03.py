def addnum(*args):
    total = 0
    for i in args:
        total += i
    print(total)

print(addnum(2,3,4,5))

def bio(**kwargs):
    print(kwargs)

bio(name="Dilwar",rollno=53)

def combine(a,b,*args,**kwargs):
    sum=a+b
    print(kwargs)
    print(args)
    return sum

combine(4,55,10,22,40,50,name="dilwar")
