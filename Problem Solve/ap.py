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
  