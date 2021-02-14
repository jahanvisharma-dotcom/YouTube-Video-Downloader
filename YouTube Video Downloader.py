#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pytube import YouTube


# In[ ]:


link = input("Enter the link ")
print("Downloding...")
YouTube(link).streams.first().download()
print("Video downloaded successfully")


# In[ ]:





# In[ ]:




