#!/usr/bin/env python
# coding: utf-8

# # E-Commerce

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


data=pd.read_csv("Ecommerce Purchases")


# In[3]:


data


# #### Q.1 1. Display Top 10 Rows of The Dataset

# In[4]:


data.head()


# In[5]:


data.head(10)


# #### Q.1. 2. Check Last 10 Rows of The Dataset

# In[6]:


data.tail()


# In[8]:


data.tail(10)


# #### Q.3. Check Datatype of Each Column

# In[12]:


data.dtypes


# #### Q.4. Check null values in the dataset

# In[13]:


data


# In[14]:


data.isnull().sum()


# #### Q.5. How many rows and columns are there in our Dataset? 

# In[15]:


data.columns


# In[16]:


len(data)


# In[17]:


data.info()


# #### Q.6. Highest and Lowest Purchase Prices.

# In[18]:


data.head()


# In[20]:


data["Purchase Price"].max()


# In[21]:


data["Purchase Price"].min()


# #### Q.7. Average Purchase Price

# In[24]:


data["Purchase Price"].mean()


# #### Q.8. How many people have French 'fr' as their Language?

# In[25]:


data.head()


# In[32]:


data[data["Language"]=="fr"].count()


# #### Q.9. Job Title Contains Engineer

# In[33]:


data.head()


# In[37]:


data[data["Job"].str.contains("engineer", case=False)]


# #### Q.10. Find The Email of the person with the following IP Address: 132.207.160.22

# In[38]:


data.head()


# In[43]:


data[data["IP Address"]=="132.207.160.22"]


# In[44]:


data[data["IP Address"]=="132.207.160.22"]["Email"]


# #### Q.11. How many People have Mastercard as their Credit Card Provider and made a purchase above 50?

# In[46]:


data.columns


# In[48]:


data["CC Provider"]


# In[51]:


data[(data["CC Provider"]=="Mastercard") & (data["Purchase Price"]>50)]


# In[52]:


data[(data["CC Provider"]=="Mastercard") & (data["Purchase Price"]>50)].count()


# In[54]:


len((data[(data["CC Provider"]=="Mastercard") & (data["Purchase Price"]>50)]))


# #### Q.12. Find the email of the person with the following Credit Card Number: 4664825258997302

# In[55]:


data.columns


# In[57]:


data[data["Credit Card"]==4664825258997302]


# In[58]:


data[data["Credit Card"]==4664825258997302]["Email"]


# #### Q.13. How many people purchase during the AM and how many people purchase during PM?

# In[59]:


data.columns


# In[60]:


data["AM or PM"].value_counts()



# #### Q.14. How many people have a credit card that expires in 2020?

# In[69]:


data.columns


# In[84]:


len(data[data["CC Exp Date"].str.contains("20")])


# In[87]:


len(data[data["CC Exp Date"].apply(lambda x:x[3:]=="20")])


# #### Q.15. What are the top 5 most popular email providers (e.g. gmail.com, yahoo.com, etc...) 

# In[101]:


list1=[]
for email in data["Email"]:
    list1.append(email.split("@")[1])


# In[103]:


data["temp"]=list1


# In[105]:


data.head()


# In[106]:


data["temp"].value_counts()


# In[107]:


data["temp"].value_counts().head(5)


# In[110]:


data["Email"].apply(lambda x:x.split("@")[1]).value_counts().head()


# In[ ]:




