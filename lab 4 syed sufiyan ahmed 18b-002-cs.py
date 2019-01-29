
# coding: utf-8

# In[1]:


#program1
#1: Practicing with simple if condition. Execute the following program with a = 400 and b = 500
a = 400
b = 500
if a==400:
    print("the value of a is equal to 400")
if a<b:
    print("the value of a is less than b")
if a>b:
    print("the value of a is greater than b")
if a!=b:
    print("the value of a is not equal to b")
if a<=b:
    print("the value of a is less than or equal to b")
if a>=b:
    print("the value of a greater than or equal to b")


# #program2
# #Practicing with simple if condition if both conditions are true using AND operator.
# a = 400
# b = 500
# c = 600
# 
# if a>b and c>a:
#     print("both conditions are true")
#     

# In[8]:


print('hello world')


# In[20]:


a=10
b=5
c=20
if a>b and c>a:
    print("Both conditions are true")


# In[13]:


print("both conditions are true")


# In[19]:


#program3
#Practicing with simple if condition if any of the condition is true using OR operator.

a = 105
b = 20
c = 200

if a>b or a>c:
    print("atleast one of the conditions are true")


# In[22]:


#program4
#Write a program which takes the lower limit and upper limit then find which of the number are prime number
l_limit=int(input("Enter lower limit range:"))
u_limit=int(input("Enter upper limit range:"))

print("prime numbers between",l_limit,"and",u_limit,"are:")
for number in range(l_limit,u_limit + 1):
    if number>1:
        for i in range(2,number):
            if(number%i)==0:
                break
        else:
            print(number)
        


# In[25]:


#program5
#Write a program which takes the initial and final values from the user then print the sum of all the numbers.

initial_value=eval(input("Enter the initial value for the range:"))
final_value=eval(input("Enter the final value for the range:"))
numbers = range(initial_value,final_value)
sum = 0
for value in numbers:
    sum = sum + value
print("the sum is", sum)    


# In[26]:


#program6
#Write a program which takes the number of rows and columns from the user and generate the values in form of list.

row_num=int(input("Enter number of rows:"))
col_num=int(input("Enter number of coloumns:"))
multi_list=[[0 for col in range(col_num)]for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col]=row*col
print(multi_list)        
            
            


# In[32]:


#program7
#Write a program which will check the data type of given data in a loop.

datalist = [300, 12.65, 5+6j, True, 'Faisal', (5, -7), [8, 52],{"color":'blue', "color":'red'}]
for item in datalist:
            print("Type of",item,"is",type(item))
            


# In[33]:


#program8
#Write a program to generate the ASCII Chart from 0 to 256.

print("\t\t\t ASCII character")

for i in range(0,256):
    print(i,"=",chr(i),end="\t")
print("\n")
      
    


# In[35]:


#program9
#Write a program to convert digital number from 0 to 16 into binary, octal and hexa-decimal number system.

print("python program to convert digital number into binary,octal and hexa-decimal number system")

for i in range(0,17):
    print("The decimal value of",i,"is:","in binary its:",bin(i),"in octal its:",oct(i),"and in hexe-decimal its:",hex(i))
print("thats the end of a program with range from 1 to 16")          
          


# In[40]:


#program10
#Write a Python program to construct the following pattern, using a nested for loop.

n = 5;
for i in range(n):
    for j in range(i):
        print('*',end="")
    print('')
    
for i in range(n,0,-1):
    for j in range(i):
        print('*',end="")
    print('')   
    
          

          
        


# In[41]:


#program11
#Write a program which calculates the vowels from the given string.

print("this program will count total number of vowels from user defined sentence")
string = input("enter your string:")
vowels = 0
for i in string:
    if(i=='a'or i=='e'or i=='i'or i=='o'or i=='u'or i=='A'or i=='E'or i=='I'or i=='O'or i=='U'):
        vowels = vowels + 1
print("Number of vowels are:")
print(vowels)
    

