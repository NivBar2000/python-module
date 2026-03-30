def add(x, y):
   b = x + y
   print(b)

def sub(x, y):
    b = x - y
    print(b)
    
def mult(x, y):
    b = x * y
    print(b)
    
def div(x, y):
    if y == 0:
        print("you can divide by 0")
    else:
        b = x / y
        print(b)
    
def oper(x, y, action):
    match action:
        case 1:
            add(x,y)
        case 2:
            sub(x,y)
        case 3:
            mult(x,y)
        case 4:
            div(x,y)