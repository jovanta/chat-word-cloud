#!/usr/bin/env python
# coding: utf-8

# In[16]:


f = open('Ochan.txt', 'r', encoding="utf8")
file_contents = f.read()


# In[17]:


num=0
for i in file_contents:
    if i == '[':
        num+=1


# In[18]:


ls=[]
tmp = 0
word = file_contents[20:]

for i in range(num):
    for x in word:
        if x == '[':
            break
        else:
            tmp+=1
    ls.append(word[:tmp])
    word=word[tmp+20:]
    tmp=0


# In[19]:


ls


# In[30]:


shakti = []
for i in ls:
    if 'Shakti Widjonarko' in i:
        shakti.append(i[19:])


# In[31]:


shakti


# In[37]:


ochan = []
for i in ls:
    if 'Ochan' in i:
        ochan.append(i[7:])


# In[38]:


ochan


# In[39]:


import pandas as pd


# In[40]:


x = pd.Series(ochan)


# In[45]:


z = pd.Series(shakti)


# In[46]:


x


# In[47]:


z


# In[ ]:




