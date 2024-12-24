#!/usr/bin/env python
# coding: utf-8

# # Sales Analysis

# ###Import necessary Libraries

# In[2]:


import pandas as pd
import os


# ### Merging 12 months of sales data into single csv file

# In[3]:


df=pd.read_csv("./Sales data/Sales_April_2019.csv")


files=[file for file in os.listdir('./Sales data')]

all_months_data=pd.DataFrame()

for file in files:
    df=pd.read_csv("./Sales data/"+file)
    all_months_data=pd.concat([all_months_data, df])
    
all_months_data.to_csv("all_data.csv",index=False)
    
    


# #Read updated dataframe

# In[4]:


ad=pd.read_csv("all_data.csv")

ad


# ### Clean data

# In[5]:


ad.info()


# In[6]:


ad.dropna(inplace=True)


# In[7]:


ad.info()


# In[8]:


ad=ad.dropna(how='all')


# In[9]:


ad.head()


# ## Find "OR" and delete it

# In[10]:


ad=ad[ad['Order Date'].str[0:2]!='Or']
ad.head()


# In[ ]:





# ### Augment data with additional column

# ## Add Month Column

# In[11]:


ad['Month']=ad['Order Date'].str[0:2]
ad['Month']=ad['Month'].astype('int32')


# In[12]:


ad.head()


# ## Add city column

# In[13]:


ad['City']=ad['Purchase Address'].apply(lambda x:x.split(',')[1])


ad.head()


# In[14]:


ad['State']=ad['Purchase Address'].apply(lambda x:x.split(',')[2].split(' ')[1])

ad.head()


# In[15]:


def get_city(address):
    return address.split(',')[1]


def get_state(address):
    return address.split(',')[2].split(' ')[1]

ad['City']=ad['Purchase Address'].apply(lambda x: f"{get_city(x)} ( {get_state(x)} )")

ad.head()


# ## What was the best month for sales How much was earned thet month?

# ## Add Sales Column

# In[16]:


ad.columns


# In[17]:


ad['Price Each'].dtype


# In[18]:


ad['Quantity Ordered'].dtype


# In[19]:


ad['Price Each']=ad['Price Each'].astype(float)


# In[20]:


ad['Quantity Ordered']=ad['Quantity Ordered'].astype(int)


# In[21]:


ad['Sales']=ad['Quantity Ordered']*ad['Price Each']


# In[22]:


ad.head()


# In[23]:


month_sales=ad.groupby('Month').sum('Sales')
month_sales


# In[24]:


import matplotlib.pyplot as plt

months=range(1,13)

plt.bar(months,month_sales['Sales'])

plt.xticks(months)
plt.ylabel('Sales in USD ($)')
plt.xlabel('Month Number')


# In[ ]:





# ## What city has Highest number of sales?

# In[25]:


results=ad.groupby('City').sum('Sales')

results



# In[26]:


import matplotlib.pyplot as plt
cities=ad['City'].unique()
cities


# In[27]:


cities=[city for city,df in ad.groupby('City')]
plt.bar(cities,results['Sales'])

plt.xticks(cities,rotation='vertical',size=8)
plt.ylabel('Sales in USD ($)')
plt.xlabel('City')
plt.show()


# In[28]:


ad.head()


# # 3.What time should we display advertisemens to maximize the likelihood of customer’s buying product?

# In[29]:


ad['Order Date']=pd.to_datetime(ad['Order Date'])


# In[30]:


ad['Hour']=ad['Order Date'].dt.hour
ad['Minute']=ad['Order Date'].dt.minute


# In[31]:


ad.head()


# In[32]:


hours=[hour for hour,df in ad.groupby('Hour')]
plt.plot(hours,ad.groupby(['Hour']).count())
plt.xticks(hours)
plt.xlabel('Hour')
plt.ylabel('Number of Orders')
plt.grid()
plt.show()


# # 4.What products are most often sold together?

# In[33]:


ad.head()


# In[34]:


df=ad[ad['Order ID'].duplicated(keep=False)]
df['Grouped']=df.groupby('Order ID')['Product'].transform(lambda x:';'.join(x))


# In[35]:


df.head()


# In[36]:


df=df[['Order ID','Grouped']].drop_duplicates()


# In[37]:


df


# In[38]:


from itertools import combinations
from collections import Counter

count=Counter()

for row in df['Grouped']:
    row_list=row.split(';')
    count.update(Counter(combinations(row_list,2)))
    
print(count)


# In[39]:


for key,value in count.most_common(10):
    print(key,value)




#   # What product sold the most? 
#   

# In[40]:


product_group=ad.groupby('Product')



# In[41]:


print(product_group)




# In[42]:


quantity_ordered=product_group.count()['Quantity Ordered']

products=[product for product,df in product_group]

plt.bar(products,quantity_ordered)
plt.xticks(products,rotation='vertical',size=8)
plt.xlabel('Product')
plt.ylabel('Quantity Ordered')
plt.show()


# In[43]:


ad.columns


# In[44]:


price=ad.groupby('Product')['Price Each'].mean().reset_index()


# In[45]:


price.columns=['Product','Mean Price']
print(price)


# In[54]:


sorteddf=price.sort_values(by='Mean Price',ascending=False)


# In[55]:


product=sorteddf['Product']
mean_price=sorteddf['Mean Price']
plt.bar(product,mean_price)
plt.xticks(product,rotation='vertical',size=8)
plt.xlabel('Product')
plt.ylabel('Mean Price')
plt.show()


# In[ ]:





# In[ ]:




