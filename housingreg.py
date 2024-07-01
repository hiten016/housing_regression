#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd   #data cleaning
import numpy as np
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib
matplotlib.rcParams["figure.figsize"]=(20,10)


# In[6]:


df1=pd.read_csv(r"C:\Users\Hiten Mahajan\Downloads\Housing.csv", sep=',',header=0)
df1.head()


# In[7]:


df1.shape



# In[8]:


df1.groupby('furnishingstatus')['furnishingstatus'].agg('count')


# In[10]:


df2=df1.drop(['prefarea','stories','hotwaterheating','basement','guestroom'],axis='columns') 
df2.head() #dropping criteria for consideration


# In[11]:


df2.isnull().sum()  # no area were the data is not there 


# In[12]:


df3=df2.dropna()   #not required already null 
df3.isnull().sum()


# In[14]:


df3.shape


# In[17]:


df3['bathrooms'].unique() #array check for unique values 


# In[18]:


df3.head()


# In[19]:


#split to dataset
#df3['bhk']=df3['size'].apply(lambda x:x.split(' ')[0])
#not required for this dataset


# In[ ]:





# In[ ]:




