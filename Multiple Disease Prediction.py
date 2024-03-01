#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# In[8]:


# loading the saved model

# loading the saved models using binary mode 'rb'
with open('Diabetes_model.sav', 'rb') as file:
    diabetes_model = pickle.load(file)

with open('heart_disease_model.sav', 'rb') as file:
    heart_disease_model = pickle.load(file)

with open('parkinsons_model.sav', 'rb') as file:
    parkinsons_model = pickle.load(file)


# In[13]:


# sidebar for navigate

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          ['Diabetes Prediction',
                          'Heart Disease Prediction',
                          'Parkinsons Prediction'],
                          default_index = 0)


# In[14]:


# diabetes prediction page

if(selected == 'Diabetes Prediction'):

    # page title
    st.title('Diabetes Prediction using ML')
    
if(selected == 'Heart Disease Prediction'):

    # page title
    st.title('Heart Disease Prediction using ML')
    
if(selected == 'Parkinsons Prediction'):

    # page title
    st.title('Parkinsons Prediction using ML')    
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




