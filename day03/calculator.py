def add(*args:int)->int:
    '''This function is used to sum multipe numbers and returnse the results of sum'''
    sum_result=0
    for i in args:
        sum_result += i
    return sum_result

def subtract(a:int,b:int)-> int:
    '''This function is used to subtract two num by taking two parameter'''
    sub=a-b
    return sub

def multiply(*args:int)->int:
    '''this function is used to multiply  multiple numbers togther'''
    mul=1
    for i in args:
        mul *= i
    return mul

def div(a:int,b:int)-> float | str:
    '''this function is used to divide two number if user inserts 0 for dividing a number it returns a string'''
    if b != 0:
        divison = a/b
    else:
        return "cannot divide by 0"
    return divison

def get_number(prompt:str)->list[int] :
    '''The get_number takes  list of strings coverts into list of integers  '''
    prompt_line=input(prompt).split()

    converted_num=[]
    for i in prompt_line:
        converted_num.append(int(i))
    return converted_num
   


print("Welcome to My calculator\n")
while True:
    print("\nadd - a\nsubtract - s\nmultiply - m\ndivision - d\nquit - q\n")
    operation_request=input("Select Operation : ")
    if operation_request == 'a':
        converted_num=get_number("Enter numbers for addtion : ")
        print(f"Addition of the numbers is: ",add(*converted_num))
    elif operation_request == 's':
        converted_num = get_number("Enter two numbers for subtractions")
        print(f"Subtraction of numbers is ",subtract(*converted_num))
    elif operation_request == "m":
        converted_num = get_number("Enter numbers for multiplication : ")
        print(f"Multiplication of the Numbers is ",multiply(*converted_num))
    elif operation_request == 'd':
        converted_num=get_number("enter numbers for division")
        print("Division is ",div(*converted_num))


    if operation_request == "q" : break