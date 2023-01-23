# 1 Find factorial of a number
# 2. Find trailing zeros of the factorial number
# Note: trailing zeros means number of zeros at the end
def zeros(n):
    count=0
    num=fact(n)
    while(num%10==0):
        count=count+1
        num=num//10
    return count
def fact(n):
    i=1
    facto=1
    while(i<=n):
        facto=facto*i
        i=i+1
    return facto

n=int(input("Enter the number:"))
output=fact(n)
print(f'The factorial of {n} is {output}')
output2=zeros(n)
print(f'The trailing zeros in {output} is {output2}')

