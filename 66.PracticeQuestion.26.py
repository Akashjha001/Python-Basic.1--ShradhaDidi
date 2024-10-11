# to find factorial of n with the help of function
n = int(input("Enter any number: "))
def calc_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print (fact)

calc_fact(n)