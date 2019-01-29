
# coding: utf-8

# In[2]:


#program1
#Practicing with simple while loop, giving them the final condition of loop.

count = 0
f = eval(input("Enter your final condition where you want to break the loop:"))

while(count<f):
    print("the value of count:",count)
    count=count+1
    print("i am using while loop",count,"time")


# In[ ]:


#program2
#Practicing with simple while loop with infinite iterations as the condition is always true.

var=1
while var == 1:
    num = eval(input("Enter a number :"))
print("you entered:",num)

print("End of loop!")
      


# In[2]:


#program3
#Write a program which takes the limit for while loop condition and sum the total amount.

n = eval(input("Enter the value to execute the while loop:"))
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i+1
print("The sum is", sum)


# In[5]:


#Program 4: Practicing with simple while loop with else condition.

i = 0
f = 10
while i<f:
    print(i,"is less than final condition")
    i=i+1
else:
    print(i,"is not less than final condition")


# In[8]:


#Program 5: Write a function f which takes one argument x, it will square the value of x and add 1 in it
#then return the answer to user.

def f(x):
    res=x**2+1
    return res


# In[16]:


def f(x):
    res = x**2 + 1
    return res
x = 2
print(x)


# In[24]:


#Program 6: Write a Python function which takes no argument and generate and print a list of first and last
#6 elements where the values are cube of numbers between 1 and 30 (both included).

def CubeValues():
    lst=list()
    for i in range(1,31):
              lst.append(i**3)
    print(1[6:]) 
    print(1[-6:])
    
CubeValues()    

