# n = int(input("enter the number:"))
# fact = 1
# i= 1
# while i<=n:
#     fact *=i
#     i += 1

# print("factorial =", fact)    

#Q2

n = int(input("enter numbers:"))
fact = 1

for i in range(1, n+1):
    fact *= i

print("fact = ", fact)    