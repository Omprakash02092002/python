#function definition

# def calc_sum(a, b):  # a, b is parameters
#     return(a + b)

# sum = calc_sum(1,2)   # function call ; 1,2 is arguments
# print(sum)

#-----------------------------------------------------------
#  average of 3 numbers:

# def calc_avg(a, b, c):
#     sum = a + b + c
#     avg =  sum / 3
#     print(avg)
#     return avg

# calc_avg(98, 97 ,95)
#-------------------------------------------------------------- 

#WAF to print the length of a list.(list is the parameter)

# cities = ["delhi", "pune","noi_da","gur_g_aon", "mumbai","chennai"]
# heroes = ["thor","iron man","captain america", "shakti man"]

# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(heroes)

#------------------------------------------------------------------------

#wap to print the element of a list in a single line.(list ia the parameter)

# cities = ["delhi", "pune","noi_da","gur_g_aon", "mumbai","chennai"]
# heroes = ["thor","iron_man","captain_america", "shakti_man"]

# def print_len(list):
#     print(len(list))

# print_len(cities)    

# def print_list(list):
#     for item in list:
#         print(item, end = " ")

# print_list(heroes)            
   
#-----------------------------------------------------------------------------------

#WAP to find the factorial of n. (n is the parameters.)

# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)

# cal_fact(5)     #120

#_______________________________________________________________________________
#WAP to convert USD to INR.

# def convert(usd_val):
#     inr_val = usd_val * 83
#     print(usd_val, "USD =", inr_val, "INR")

# convert(45)    
        

#_________________________________________________________________________________
# WAP to check thr single number of even/odd and string. (using if-else loop)

# def check_even_odd(n):
#     if n %2 ==0 :
#         print( n ,"this is a 'EVEN' value")
#     else:
#         print(n ,"this is 'ODD' value.")

# check_even_odd(7)  

#________________________________________________________________________

# WAP to check thr single number of even/odd and string. (using for loop)


def check_even_odd(n):
    for i in range(n , n+1):
        if(i % 2 == 0):
            print(i ,"is EVEN")
        else:    
            print(i ,"is ODD")

num = int (input("enter a number: "))
check_even_odd(num)
