def show_his(n):
    try:
        with open("C:\\Users\\Administrator\\Desktop\\python calc\\sample.txt","r") as file:
            lin=file.readlines()
            for line in lin[-n:]:
                print(line,end="")
    except Exception as e:
        print("Error occure",e)

def to_file(a):
       with open("C:\\Users\\Administrator\\Desktop\\python calc\\sample.txt","a") as f:
            f.write(f"{a}\n")


print("Welcome to Calculator:")
while True:
    num=int(input("Enter value:"))
    oper=(input("Enter Opration (+ / - / * / / / **):"))
    num1=int(input("Enter second value:"))

    if oper=="+":
        plus=f"{num} {oper} {num1} = {num+num1}"
        print(f"{num} {oper} {num1} = {num+num1}")
        to_file(plus)


    elif oper=="-":
        minus=f"{num} {oper} {num1} = {num-num1}"
        print(f"{num} {oper} {num1} = {num-num1}")
        to_file(minus)


    elif oper=="*":
        mul=f"{num} {oper} {num1} = {num*num1}"
        print(f"{num} {oper} {num1} = {num*num1}")
        to_file(mul)


    elif oper=="/":
        try:
           div=f"{num} {oper} {num1} = {num/num1}"
           print(f"{num} {oper} {num1} = {num/num1}")
           to_file(div)

        except Exception as e:
            print(e)


    elif oper=="**":
        powe=f"{num} {oper} {num1} = {num**num1}"
        print(f"{num} {oper} {num1} = {num**num1}")
        to_file(powe)

    else:
        print("Invalid Choice")
    
    choi=input("Enter 1 for calculating again 2 for exit 3 for history:")
    if choi=="1":
        continue
    elif choi=="3":
        nn=int(input("Enter the number of calculation history you want:"))
        show_his(nn)

    cho=input("\nEnter 1 for calculating again 2 for exit:")
    if cho=="1":
        continue
    else:
        break
print("Thanks for using calculator")
print("Created by Bandhan Hardiya")




 