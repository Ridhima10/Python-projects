
sum=0
while True:
    user_input=input("Enter the amount you want to add and Press q to know your bill: \n")
    if user_input!='q':
        sum=sum+int(user_input)

    else:
        print(f"Your total bill is {sum}. Thanks for shopping with us. Visit again :)")
        break