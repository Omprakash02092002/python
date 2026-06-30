#__recursive function:

# def show(n):
#     if (n == 0) :     # ----base case-----------
#         return
        
#     print(n)
#     show(n - 1)

# n = int(input("enter a number :"))
# show(n)        

#_______________________________________________________________________

#--- find factorial num.-----

# def fact(n):
#     if (n == 1 or n ==0):
#         return 1

#     return fact(n-1) * n

# print(fact(int(input("enter the number :"))))

#________________________________________________________________________

#Q---Write a recursive function to calculate the sum of first n natural numbers.--

# def calc_sum(n):
#     if (n == 0):
#         return 0
    
#     return calc_sum(n-1) + n

# sum = calc_sum(int(input("enter the number :")))
    
# print("natural number of sum : ",sum)

#----------------___________________________--------------------------------

#Q---Write a recursive function to print all elements in a list.
#(Hint: use list & index as parameters.)

def print_list(list , idx = 0):
    if(idx == len(list)):
        return

    print(list[idx])
    print_list(list, idx + 1) 

fruits = ["mango", "litchi", "apple", "banana"]

print_list(fruits)

