
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[3]:


from PIL import Image


# In[4]:


pic = Image.open('00-puppy.jpg')


# In[6]:


type(pic)


# In[8]:


pic_arr=np.asarray(pic)


# In[9]:


type(pic_arr)


# In[10]:


pic_arr


# In[11]:


pic_arr.shape


# In[12]:


plt.imshow(pic_arr)


# In[13]:


pic_red = pic_arr.copy()


# In[14]:


plt.imshow(pic_red)


# In[19]:


# R G B
# Red Channel values 0 no red, pure black -255 full pure red
plt.imshow(pic_red[:,:,0]) 


# In[18]:


# R G B
plt.imshow(pic_red[:,:,0],cmap='gray') 


# In[20]:


# How to zero out green channel
pic_red[:,:,1] = 0


# In[21]:


plt.imshow(pic_red)


# In[23]:


# How to zero out blue channel
pic_red[:,:,2] = 0
plt.imshow(pic_red)


# In[24]:


pic_red.shape

