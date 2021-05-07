#!/usr/bin/env python
# coding: utf-8

# # Automatic Card Generation from Template 
# ## *Image Manipulation using Python*

# In[86]:


import pandas as pd
from PIL import Image, ImageDraw, ImageFont


# In[87]:


from make_qr_code import generate_qr


# In[88]:


df = pd.read_csv("students.csv")
df = df.dropna()


# In[89]:


df


# In[90]:


records = df.to_dict(orient='record')


# In[121]:


def generate(data):
    
    A= data['id']
    B= data['name']
    C= data['branch']
    D= data['year']
    return generate_qr(A, B, C, D)
    


# In[122]:


for record in records:
    qr = generate(record)
    qr.save(f"photos/{record['id']}.jpg")


# In[123]:


font = ImageFont.truetype("OpenSans-Semibold.ttf", size=23)


# In[132]:


def generate_card(data):
    template = Image.open("template3.jpg")
    pic2 = Image.open(f"original/{data['id']}.jpg").resize((118, 135), Image.ANTIALIAS)
    template.paste(pic2, (88,123, 206, 258))
    draw = ImageDraw.Draw(template)
    pic = Image.open(f"photos/{data['id']}.jpg").resize((110, 125), Image.ANTIALIAS)
    template.paste(pic, (182, 368, 292, 493))
    draw = ImageDraw.Draw(template)
    draw.text((18, 277), "Name : "+data['name'], font=font, fill='black')
    draw.text((18, 327), "Roll No. : " + str(data['id']), font=font, fill='black')
    draw.text((18, 375), "Branch : "+data['branch'], font=font, fill='black')
    draw.text((18, 426), "Year : "+str(data['year']), font=font, fill='black')
    return template


# In[133]:


for record in records:
    card = generate_card(record)
    card.save(f"cards/{record['id']}.jpg")


# In[ ]:




