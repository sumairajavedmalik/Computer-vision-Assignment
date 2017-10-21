
# coding: utf-8

# # Linear Regression
# 

# In[2]:

import numpy as np
import matplotlib.pyplot as plt


# In[3]:

diameter = [6,8,10,14,18]
price = [7,9,13,17.5,18]


# In[4]:

#varirnce of x
a = np.var(diameter, ddof=1)
b = np.cov(diameter, price, ddof=1)[0][1]
#b = np.cov(diameter,price, ddof =1)
print ('a = ', a)
print ('b = ', b)


# In[5]:

beta = b/a
print ('beta = ', beta)


# In[6]:

#calculate  mean of x
x_bar = sum(diameter) / len(diameter)
print(x_bar)


# In[7]:

#calculate mean of y
y_bar = sum(price) / len(price)
print(y_bar)


# In[10]:

alpha = y_bar - beta*x_bar
print(alpha)


# In[11]:

x = np.array(diameter)
y = alpha + beta * x
print(y)


# In[14]:

ar = np.array(price)
SS_tot = sum((ar - y_bar)**2)
print(SS_tot)
f_xi = np.array(y)
SS_res = sum((ar - f_xi)**2)
print(SS_res)


# In[16]:

plt.scatter(diameter, price)
plt.xlabel("Diameter")
plt.ylabel("price")
plt.plot(diameter,y)
plt.show()


# # LOOPS

# In[2]:

from collections import defaultdict

document = ["Hello","World","new","Hello","new"]
word_counts = defaultdict(int)
#word_counts = {};

for i in document:
    word_counts[i] +=1;

print(word_counts)


# In[3]:

from collections import Counter

document = ["Hello","world","World","new","Hello","new","Hello","Hello","new"]

c = Counter(document)
print(c);
print("----");
for word, count in c.most_common(2):
    print(word)
    print(count)


# # List
# 

# In[ ]:


studentslist = ["zeeshan","shahzaib","malika"]
print("Welcome to student portal")
print("Please enter 1 to list student names")
print("Please enter 2 to add student names")
print("Please enter 3 to search student names")
print("Please enter 4 to delete particular student names")
print("Please enter 5 to sort student names")
print("enter 6 to exit")

while(True):
    user_input = int(input("Enter of your choice"))

    if user_input == 1:
        for studentnames in studentslist:
            print(studentnames)
    elif user_input == 2:
        addname = input("Enter name to add")
        studentslist.append(addname)
        print(studentslist)
    elif user_input == 3:
        userinput = input("Search for a student name")
        if userinput in studentslist:
            print("found")
        else:
            print("not found")
    elif user_input == 4:
        userinput = input("Enter student name to delete")
        if userinput in studentslist:
            studentslist.remove(userinput)
            print(userinput + " deleted")
        else:
            print("not found")

    elif user_input == 5:

            studentslist.sort()
            print("Sorted")
            print(studentslist)

    elif user_input == 6:
        exit()



# # Functions

# In[ ]:

from functools import partial
def exp(base, power):
    return base ** power
two_to_the = partial(exp, 2) # is now a function of one variable
print(two_to_the(3))


# In[ ]:

def is_even(x):
    """True if x is even, False if x is odd"""
    return x % 2 != 0
x_evens = [x for x in xs if is_even(x)]
print(x_evens)


# # Variables

# In[ ]:

players = ['charles', 'martina', 'michael', 'florence', 'eli']
newPlayers = players[-3:-1]
newPlayers1 = players[2:4]
print(newPlayers)
print(players)


# In[ ]:

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3,4]
list3 = zip(list1, list2)

for i,j in list3:
    print(i,j)


# In[ ]:



