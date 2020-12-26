#!/usr/bin/env python
# coding: utf-8

# In[9]:


f = open('Ochan.txt', 'r', encoding="utf8")
file_contents = f.read()


# In[8]:


num=0
for i in file_contents:
    if i == '[':
        num+=1


# In[7]:


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


# In[10]:


ls


# In[ ]:




