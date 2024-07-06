#!/usr/bin/env python
# coding: utf-8

# # Create a Bar Chart and Histogram to visualize distribution of categorical and continuous variable such as the distribution of Age or Gender in a population

# ## Import Libraries

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn
import scipy


# In[2]:


df = pd.read_csv('train.csv')


# In[3]:


df.head()


# In[4]:


df.sample()


# In[5]:


df.shape


# In[6]:


df.info()


# # Barplot to visualize the distribution of categorical and Age/Gender variable

# In[8]:


sns.barplot(x=df['Pclass'],y=df['Age'])


# In[9]:


sns.barplot(x=df['Pclass'],y=df['Age'],hue=df['Sex'])


# In[10]:


df.isnull().mean()*100


# # Histogram

# In[ ]:


plt.hist(df['Age'],bins=)

