a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
def max_at_three(a,b,c):
    if a>=b and a>c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
print(max_at_three(a,b,c))
