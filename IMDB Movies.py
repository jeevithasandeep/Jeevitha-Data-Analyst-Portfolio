#!/usr/bin/env python
# coding: utf-8

# # 1. Display Top 10 Rows of The Dataset

# In[2]:


import pandas as pd


# In[3]:


import numpy as np


# In[4]:


import matplotlib.pyplot as plt


# In[5]:


import seaborn as sns


# In[100]:


df=pd.read_csv('movies_initial.csv')


# In[7]:


df


# In[8]:


df.head(10)


# # 2. Check Last 10 Rows of The Dataset

# In[9]:


df.tail(10)


# # 3. Find Shape of Our Dataset (Number of Rows And Number of Columns)

# In[10]:


df.shape


# In[11]:


print("Rows",df.shape[0])
print("Columns",df.shape[1])


# # 4. Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement

# In[12]:


df.info()


# # 5. Check Missing Values In The Dataset

# In[13]:


df.isnull().sum()


# # 6. Drop All The  Missing Values

# In[14]:


df1=df.fillna(value=0)


# In[15]:


df1.info()


# In[16]:


df.isnull().sum()


# In[17]:


df.columns


# In[18]:


type_dct = {str(k): list(v) for k, v in df.groupby(df.dtypes, axis=1)}


# In[19]:


type_dct


# In[20]:


df2=df.select_dtypes(include="O").fillna(method="pad")


# In[21]:


df2.isnull().sum()


# In[22]:


df2.dropna(inplace=True)


# In[23]:


df2.info()


# # 7.Check for duplicate data

# In[24]:


df2.duplicated().any()


# In[25]:


# id any duplicates found:    df.drop_duplicates()


# # 8. Get Overall Statistics About The DataFrame

# In[26]:


df2.describe(include='all')


# # 9.Display Title of The Movie Having Runtime Greater Than or equal to 180 Minutes
# 

# In[27]:


df.columns


# In[28]:


df['runtime'] = df['runtime'].str.replace('min', '')


# In[29]:


df['runtime'] = pd.to_numeric(df['runtime'], errors='coerce')


# In[30]:


df['runtime'] = df['runtime'].fillna(0).astype(int)


# In[31]:


df['runtime']


# In[32]:


df[df['runtime']>=180]['title']


# # 10. In Which Year There Was The Highest Average Voting?

# In[33]:


df['year'] = df['year'].str.extract('(\d{4})').astype(int)


# In[34]:


df['imdbVotes'] = df['imdbVotes'].fillna(0)


# In[35]:


df.groupby('year')['imdbVotes'].mean().sort_values(ascending=False).head(10)


# In[36]:


sns.barplot(x='year',y='imdbVotes',data=df)
plt.title('Votes by Year')
plt.show()


# In[37]:


df.info()


# In[38]:


top_10=df.groupby('year')['imdbVotes'].mean().sort_values(ascending=False).head(10)
top_10.plot(kind='bar')


# # #11. Display Top 10 Lengthy Movies Title and Runtime

# In[67]:


df_sorted = df.sort_values(by='runtime', ascending=False).head(10)


# In[69]:


df_sorted[['runtime','title']]


# # 12.Display Number of Movies Per Year

# In[71]:


movies_per_year=df.groupby('year')['title'].count()


# In[72]:


movies_per_year


# # 13.Count Number of drama Movies

# In[101]:


df['genre']


# In[102]:


df['genre'].str.contains("drama",case=False).fillna(0)


# In[103]:


df1['genre']=df['genre'].str.contains("drama",case=False).fillna(0)


# In[104]:


count=df1['genre'].sum()


# In[105]:


print(count)


# # 14.Find Unique Values From Genre 

# In[93]:


df.columns


# In[106]:


df['genre']


# In[109]:


list1=[]
for item in df['genre']:
    list1.append(item.split(','))


# In[110]:


list1


# In[112]:


one_d=[]
for value in list1:
    for value1 in value:
        one_d.append(value1)
        
one_d


# In[113]:


uni_list=[]
for uni1 in one_d:
    if uni1 not in uni_list:
        uni_list.append(uni1)
        
uni_list


# In[115]:


len(uni_list)


# 

# In[119]:





# In[ ]:




