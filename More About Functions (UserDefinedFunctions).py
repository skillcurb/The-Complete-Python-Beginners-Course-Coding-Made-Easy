#!/usr/bin/env python
# coding: utf-8

# <h2>
# Lecture 27: User-Defined Functions
# </h2>

# <b> More on Funcitons</b>

# In[5]:


# function to guess the lucky number
def luckyNum(): 
    lucky_num = 10
    number = 0
    while(number != lucky_num):
        number = int(input('Enter a number: '))
        if number == lucky_num:
            print('You guessed it correctly')
        else:
             print('Sorry incorrect, try again')


# In[8]:


#calling the function
luckyNum()


# In[9]:


#Program to calculate Billing Invoice
def calculateInvoice(data):
    billing_amount = 0
    for i in data.values():
        billing_amount =  i + billing_amount
    return billing_amount 
#user order
order = {'Fried rice':50,'Shashlik':75,'Burger':10,'Steak':80,'Pie':12}
#calling of function
total = calculateInvoice(order)
print("Your billing amount = ${}".format(total))


# In[ ]:




