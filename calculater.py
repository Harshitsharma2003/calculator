def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def rem(x,y):
    return x%y

print("Select operation. ")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
print("5.rem")

while True:
    Choice = input("Enter choice(1/2/3/4/5): ")
    
    if Choice in ('1','2','3','4','5'):
        try:
            n1 = float(input("enter 1st num : "))
            n2 = float(input("enter 2nd num : "))
        except ValueError:
            print("invalid input . please enter a num : ")
            continue

        if Choice == '1':
            print(f"{n1} + {n2} = {add(n1,n2)}")

        elif Choice == '2':
            print(f"{n1} - {n2} = {sub(n1,n2)}")

        elif Choice == '3':
            print(f"{n1} * {n2} = {mul(n1,n2)}") 

        elif Choice == '4':
            print(f"{n1} / {n2} = {div(n1,n2)}") 

        elif Choice == '5':
            print(f"{n1} % {n2} = {rem(n1,n2)}") 

        next_calculation = input("Lets do next calculation ? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("invalid input")