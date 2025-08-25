# Write a program to reverse a string without using built-in functions.
name = "Abrar"
reverseString = ""
for char in name:
  reverseString = char+reverseString
print(reverseString)

#Swap two numbers without using a third variable.
a = 5;
b = 10;
print("Before Exchange Value")
print("a value ",a)
print("b value ",b)
a = a+b;
b = a-b
a = a-b
print("After Exchange Value")
print("a value ",a)
print("b value ",b)

#Write a program to check if a number is prime.
num = int(input("Enter the Number: "))

if num > 1:
    for i in range(2, num):
        if (num % i == 0):   
            print(num, "is NOT a prime number")
            break
    else:
        print(num, "is a Prime number")
else:
    print(num, "is NOT a prime number")

#Write code to print the Fibonacci series up to N terms.
a = 0
b = 1
n = 10
for i in range(n):
  print(a,end = " ")
  c = a+b
  a = b;
  b = c;


#Find factorial of a number using recursion.
def factorial(x):
    if(x==1):
        return 1;
    return x*factorial(x-1)
num =  3
result = factorial(num)
print("Factorial of {} is {}".format(num,result))

#Write a program to check if a string is a palindrome.
name = "Abrar"
reversestring  = ""
for i in range(len(name)-1,-1,-1):
  reversestring = reversestring+name[i];
  print(reversestring)
if(reversestring == name):
  print("Yes its palindrome ",name)
else:
  print("No its not palindrome ",name)
  

#Find duplicates in an array.
a = [1,2,3,4,2,7,8,8,3,4]
for i in range(0,len(a)):
  for j in range(i+1,len(a)):
    if a[i] == a[j]:
      print(a[j])


#Sort an array without using a built-in function.
def bubbleSort(a):
    for i in range(0, len(a)):
        for j in range(0, len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

a = [1,2,3,4,2,7,8,8,3,4]
print("Bubble Sort:", bubbleSort(a))

#Find the largest and smallest number in an array.
arr =  [5, 2, 9, 1, 7]
smallest = arr[0]
Largest = arr[0]
for num in arr:
  if num < smallest:
    smallest = num
  if num > Largest:
    Largest = num
print("Smallest Element ",smallest)
print("Largest Element", Largest)

#Write a program to count vowels in a given string.
name = "Abrar"
count = 0;
for char in name:
  if char in "AaEeIiOoUu":
    count = count+1;
print(count)

#Remove Dublicate Character From String
name  = "Abrar"
result  = ""
for char in name:
  if char not in result:
    result = result+char
print(result)


#Make Pattern #
# *
# *1
# *123
# *+1A3
# *12+-Ab
# *12+A-bcd

nums = "123456789"
specials = "+-"
uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowers = "abcdefghijklmnopqrstuvwxyz"
n = 6
for i in range(n):
  line = "*"
  if i == 0:
    pass
  elif i == 1:
    line = line+nums[0]
  elif i == 2:
    line = line +nums[0]+ nums[1]+nums[2]
  elif i == 3:
    line = line + specials[0]+nums[0]+uppers[0]+nums[2]
  elif i == 4:
    line = line + nums[0] + nums[1]+specials[0]+specials[1]+uppers[0]+lowers[1]
  elif i == 5:
    line = line + nums[0] + nums[1]+specials[0]+uppers[0]+specials[1]+lowers[1]+lowers[2]+lowers[3]
  print(line)
  
#Pattern Use
# *
# * *
# * * *
# * * * *
# * * * * *
n= 5;
for i in range(n+1):
  for j in range(i):
    print("*",end="")
  print()
  
  #PATTERN USE
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 

n = 5
for i in range(0,n):
  for j in range(0,n-i-1):
    print(end=" ")
  for k in range(0,i+1):
    print("*",end=" ")
  print()
  
#2D Array -> Write a program to take input and print a 2D array.
row = int(input("Please Enter Row: "))
col = int(input("Please Enter Col: "))
matrix= []
for i in range(row):
    row = []
    for j in range(col):
        val = int(input(f"Please Enter at: [{i}] [{j}]"))
        row.append(val)
    matrix.append(row)
for val in matrix:
    for j in val:
        print(j,end=" ")
    print()
  
print("Sum of All Elements")
sum = 0
for i in matrix:
    for val in i:
        sum = sum+val
print(sum)
print("Maximum and Minimum Value find from 2D matrix")
minimum = matrix[0][0]
maximum = matrix[0][0]
for i in matrix:
    for val in i:
        if val > maximum:
            maximum = val
        if val < minimum:
            minimum = val
print("Maximum Value: ",maximum)
print("Minimum Value: ",minimum)

#Search an element in a 2D array
matrix = [
    [5, 2, 8],
    [1, 9, 4]
]
findvalue = 10
found = False
for i in range(len(matrix)):
    for value in range(len(matrix[i])):
        if matrix[i][value] == findvalue:
            print("Found Element in the array 2D: ",value)
            found = True
if not found:
        print(f"Element {findvalue} not found in the array")
        
        
#Print the row-wise and column-wise sum.
matrix = [
    [5, 2, 8],
    [1, 9, 4]
]
sum = 0;
print("Row Wise Sum the Elements")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        sum = sum+matrix[i][j]
    print(sum)
print("Col wise Sum the Elements")
for i in range(len(matrix[0])):
    sum =0;
    for j in range(len(matrix)):
        sum = sum + matrix[j][i]
    print(sum)
    
#Matrix Transpose
matrix  = [
    [1,2,3],
    [4,5,6]
]
rows = len(matrix)
cols = len(matrix[0])
transpose = [[0 for _ in range(rows)] for _ in range(cols)]
print(transpose)
for i in range(rows):
    for j in range(cols):
        transpose[j][i] = matrix [i][j]
print("Print Transpose Matrix")
for i in transpose:
    print(i)


#Find Second Largest Number in an Array (without using built-in functions like max, sort)
arr = [12, 35, 1, 10, 34, 1]
secondLarges = -999999
largest = -999999
for i in range(len(arr)):
    if arr[i] > largest:
        secondLarges = largest
        largest = arr[i]
    elif arr[i] > secondLarges and arr[i] != largest:
        secondLarges = arr[i];
print("Largest Element : ",largest)
print("Second Largest Element : ",secondLarges)
