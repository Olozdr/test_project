a=int(input("Enter a:"))
b=int(input("Enter b:"))
operation=input("Input operation:")
def calculator(a:int, b:int,operation:str):
    match operation:
        case "+": return a+b
        case "-": return a-b
        case _: return ("Error")
c=calculator(a,b,operation)
print(c)

