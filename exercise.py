#!/usr/bin/env python
# coding: utf-8

# # Python Crash Course Exercises 
# 
# This is an optional exercise to test your understanding of Python Basics. If you find this extremely challenging, then you probably are not ready for the rest of this course yet and don't have enough programming experience to continue. I would suggest you take another course more geared towards complete beginners, such as [Complete Python Bootcamp](https://www.udemy.com/complete-python-bootcamp)

# ## Exercises
# 
# Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.

# ** What is 7 to the power of 4?**

# In[2]:


7 ** 4


# ** Split this string:**
# 
#     s = "Hi there Sam!"
#     
# **into a list. **

# In[6]:


s = "Hi there Sam!"


# In[7]:


s.split()


# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.

# In[9]:


planet = "Earth"
diameter = 12742


# In[11]:


s = "The diameter of {0} is {1} kilometers.".format(planet, diameter)
print(s)


# ** Given this nested list, use indexing to grab the word "hello" **

# In[12]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


# In[14]:


lst[3][1][2][0]


# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# In[16]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[22]:


d['k1'][3]['tricky'][3]['target'][3]


# ** What is the main difference between a tuple and a list? **

# In[23]:


# Tuple is immutable


# ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**

# In[30]:


def domainGet(email):
    return email.split('@')[1]


# In[31]:


domainGet('user@domain.com')


# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

# In[34]:


def findDog(str):
    if 'dog' in str.lower():
        return True
    return False


# In[35]:


findDog('Is there a dog here?')


# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

# In[36]:


def countDog(str):
    count = 0
    for element in str.lower().split():
        if element == 'dog':
            count += 1
    return count


# In[37]:


countDog('This dog runs faster than the other dog dude!')


# ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
# 
#     seq = ['soup','dog','salad','cat','great']
# 
# **should be filtered down to:**
# 
#     ['soup','salad']

# In[39]:


seq = ['soup','dog','salad','cat','great']


# In[42]:


list(filter(lambda element: element[0] == 's',seq))


# ### Final Problem
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **

# In[47]:


def caught_speeding(speed,is_birthday):
    status=''
    if is_birthday == False:
        if speed <= 60:
            status = 'No Ticket'
        elif speed >= 61 and speed <= 80:
            status = 'Small Ticket'
        else:
            status = 'Big Ticket'
    else:
        if speed <= 65:
            status = 'No Ticket'
        elif speed >= 66 and speed <= 85:
            status= 'Small Ticket'
        else:
            status= 'Big Ticket'
    return status


# In[51]:


caught_speeding(81,True)


# In[50]:


caught_speeding(81,False)


# # Great job!
