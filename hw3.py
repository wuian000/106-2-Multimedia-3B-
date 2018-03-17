
# coding: utf-8

# In[1]:

i=4


# In[2]:

type(i)


# In[3]:

f=3.14


# In[4]:

type(f)


# In[5]:

b=True


# In[6]:

type(b)


# In[7]:

hungry=True


# In[8]:

sleep=False


# In[9]:

not hungry


# In[10]:

hungry and sleep


# In[11]:

ss="This is a string."


# In[12]:

ss


# In[13]:

a=[1,2,3,4,5]


# In[14]:

type(a)


# In[15]:

print(a)


# In[16]:

len(a)


# In[17]:

a[1]


# In[18]:

a[0:2]


# In[19]:

a[1:]


# In[20]:

a[-1]


# In[21]:

a[:-2]


# In[24]:

from skimage import io
img1 = io.imread('p6CVo6Cck6eW.jpg',as_grey=True)
print(type(img1.shape))
print(img1.shape)
io.imshow(img1)
io.show()


# In[ ]:



