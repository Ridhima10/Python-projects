# Write a program which will keep adding a stream of numbers inputted by the user.The adding stops as soon as the user presses q key on the keyboard.
sum=0
print("Welcome to the store!!")
while True:
    user_input=input("Enter the amount you want to add and Press q to know your bill: ")
    if user_input!='q':
        sum=sum+int(user_input)

    else:
        print(f"Your total bill is {sum}. Thanks for shopping with us. Visit again :)")
        break
    
# i = 0
# j = 0
# l = []
# while True:
#     a = (input("\nenter a price or press q to get total : "))
#     if a != 'q':
#         i = i + int(a)
#         j = j + 1 
#         l.append(int(a)) # add all price in empty list l = []
#     else:
#             str_to_string = [str(int) for int in l] # convert all integer in string avl in list
#             final = "\n".join(str_to_string) # using join split string list
#             print(f"{final}")
#             print("dhruv store")
#             print(f"total bill is {i} . thank you visit again")
#             exit()