# def min_max(numbers):
#     if isinstance(numbers,(tuple)):
#         return [min(numbers) ,max(numbers)]
#     else:
#         print("please inter list  it is accept only  list")


# ab=min_max([4, 5, 89,9870,5678,490,20])
# print(ab)



# def even_number(numbers):
#     result=0
#     if isinstance(numbers,(list,tuple,)):
#         for i in numbers:
#             if i % 2 == 0:
#                 result+=i
#         return  result
# ab=even_number([4, 5, 89,9870,5678,490,20])
# print(ab)





#     def even_number(numbers):
#     result = 0
#     if isinstance(numbers, (list, tuple)):
#         for i in numbers:
#             if i % 2 == 0:
#                 result += i
#         return result
#     else:
#         print("Please enter a list or tuple")

# ab = even_number([4, 5, 89, 9870, 5678, 490, 20])
# print(ab)
        

# def contains_vowel_any(hw):
#     voewl="aeiouAEIOU"
#     count=0
#     for i in any(char in voewl for char in hw):
#         count+=1


# def sum(a,b):

#     return a+b

# total_sum=sum(3,5)
# print(total_sum)
    
# def add_one(g):
#    if isinstance(g,(int,float)):
#       return g + 1
#    else:
#       print("enter only numbers")

# total=add_one(6)
# print(total)


# def odd_even(numb):
#     if isinstance(numb,(int, float)):
#        return  numb % 2 == 0
#     else:
#         return ("enter numbers")

# check_num=odd_even(23)
# print(check_num)


# def minute_to_sec(min):
#     if isinstance(min,(int, float)):
#         return min*60
#     else:
#         return ('enter numbers')
# abd=minute_to_sec(5)
# print(abd)

# def area_of_triangle(b,h):
#     if isinstance(b,(int, float)) and isinstance(h,(int,float)):
#         return (b*h)/2
#     else:
#         return ("enter numbers")

# avs=area_of_triangle(3,4)
# print(avs)


# def last_element(stri):
#     if isinstance(stri,(list)) and len(stri) > 0:
#         return stri[-1]
#     else:
#         return "the list empty"
# stri=last_element([])
# print(stri)

# def ramainder_check(x,y):
#     if isinstance(x,(float,int)) and isinstance(y,(float,int)):
#         if y==0:
#             return ("any number canot devide bty 0")
#         return x % y
#     else:
#         return ("enter numbers")

 
# asdf=ramainder_check(56,10)
# print(asdf)


# def nga_pose_check(numbers):
#     if isinstance(numbers,(int,float)):
#         return numbers > 0
        
#     else:
#         return "enter only numbwr"
# adfg= nga_pose_check(-4)
# print(adfg)



# def hours_to_second(reqsec):
#     if isinstance(reqsec,(int,float)):
#         return reqsec*3600
#     else:
#         return ('enter numbers')
    
# dfdh=hours_to_second(12)
# print(dfdh)




# def rectangle_area_premeter(l,w, operation):
#     if isinstance(l,(int,float)) and isinstance(w, (int, float)):
#       if operation == "area":
#            return l * w
#       elif  operation == "perimeter":
#             return 2 * (l + w)
#       else:
#           return  "invalid operation"
#     else:
#         "invalid operation"

# print(rectangle_area_premeter(23,23,"perimeter"))     


# Write a function that takes two numbers and returns

# "x is greater" if the first number is larger

# "y is greater" if the second number is larger

# "both are equal" if they are the same



# def which_grater(x,y,z):
#     if isinstance(x, (float,int)) and isinstance(y, (float,int)) and isinstance(z, (float,int)):
#         if x > y and x > z:
#             return ("x is greater")
#         elif y > x and y > z:
#             return ("y is greater")
#         elif z > x and z > y:
#             return ("z is greater")

#         else:
#             return ("the tree are equal")
#     else:
#         return ("enter number")
# print(which_grater(565767,485969,364657))



# Write a Python function that checks if a given year is a leap year.
# A leap year happens if:

# The year is divisible by 4,

# But not divisible by 100,

# Except when it is also divisible by 400.

# def  leap_year_happens(year):
#     if isinstance(year,(float, int)):
#         if (year % 4 ==0 and  year % 100 != 0) or (year % 400 ==0):
#             return True
#         else:
#             return False
#     else:
#         return ("enter numbers")
    
# print(leap_year_happens(1996))







# Write a Python function that:

# Takes a list of numbers as input.

# Returns the sum of all even numbers in the list.

# ✅ Requirements:

# Check that the input is a list.

# Ignore non-number elements.

# If the list is empty or has no even numbers, return 0.


# def sum_even_num(numbers):
#     total=0
#     if isinstance(numbers,list):
#         for number in numbers:
#             if isinstance(number,(int,float) ) and number%2==0:
#                  total += number
#         return total
#     else:
#         return "enter a list of numbers"
# print(sum_even_num([34,56,7,89,87,6,8]))

# Question 16: Count Vowels
# Write a Python function that:
# Takes a string as input.
# Counts and returns the number of vowels (a, e, i, o, u, both uppercase and lowercase).
# ✅ Requirements:
# Ignore non-letter characters.

# Works for both uppercase and lowercase letters.
    
# def count_vowel(strings):
#     count=0

#     vowels="aioeuAIOEU"
#     if isinstance(strings,str):
#         for char in strings:
#             if char in vowels:
#                 count+=1
#         return count
#     else:
#         return("enter string")

# print(count_vowel("welcom to abdutech"))      

# 💪 Question 17: Find the Maximum Number in a List
# Write a Python function that:
# Takes a list of numbers as input.
# Returns the largest number in the list.
# ✅ Requirements:
# Use a for loop to find the maximum manually (don’t use max() yet).
# If the list is empty, return "empty list".
# Check that the input is a list.



# def max_number(numbers):
#     if isinstance(numbers,(list,tuple)):
#         for num in numbers:
#             return max(num)
#         else:
#             return(" the list is empty")
#     else:
#         return ("enter list")

# print(max_number[23,45,67,87,345,678,987,675])    

# Write an algorithm (in Python) 
# that takes a sentence as input and reverses the order of words,
# but does not reverse the words themselves. 

# def  reverses_the_order(revword):
#         if isinstance(revword,(str)):
#                 split_revword=revword.split()
#       reversed_split_revword = split_revword[::-1]
#       joint_split_revword= "".join(reversed_split_revword)
#    return joint_split_revword
 
 
#  print(reverses_the_order("welcom to my python program"))    

# def  reverses_the_order(revword):
#     if isinstance(revword,(str)):
#         split_revword=revword.split()
#         reversed_split_revword = split_revword[::-1]
#         joint_split_revword = " ".join(reversed_split_revword)
#     else:
#         return("enter  only strings")
#     return joint_split_revword
# print(reverses_the_order("welcom to my python program"))
         


def palindrome_check(palindrome):
    return  palindrome == palindrome[::-1]

print(palindrome_check("racecar"))
print(palindrome_check("abdu"))


























   
      
       
    



    

