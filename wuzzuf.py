#!/usr/bin/env python
# coding: utf-8

# # Wuzzuf Web Scraping

# In[121]:


import requests
from bs4 import BeautifulSoup


# ### "machine learning" jobs scraping in Egypt 

# In[122]:


urls=["https://wuzzuf.net/search/jobs/?q=machine%20learning%20in%20egypt&a=hpb"]
urls+= [f"https://wuzzuf.net/search/jobs/?a=navbg&q=machine%20learning%20jobs%20in%20egypt&start={i}"for i in range(1,3)]
urls


# In[123]:


for url in urls :
    response=requests.get(url)


# In[124]:


response


# In[125]:


all_titles=[]
for url in urls:
    soup=BeautifulSoup(response.content,"lxml")
    titles=[title.text for title in soup.find_all("h2",{"class":"css-m604qf"})]
    all_titles.extend(titles)


# In[126]:


soup


# In[127]:


all_titles


# In[128]:


all_links=[]
for url in urls:
    links = [link.a["href"] for link in soup.find_all("div", {"class": "css-pkv5jc"})]
    all_links.extend(links)


# In[129]:


all_links


# In[130]:


all_locations=[]
for url in urls:
    locations=[location.text for location in soup.find_all("div",{"class":"css-d7j1kk"})]
    all_locations.extend(locations)


# In[131]:


all_locations


# In[132]:


all_occupations=[]
for url in urls:
    occupations=[occupation.text for occupation in soup.find_all("div",{"class":"css-1lh32fc"})]
    all_occupations.extend(occupations)


# In[133]:


all_occupations


# In[134]:


all_descriptions=[]
for url in urls:
    descriptions=[description.text for description in soup.find_all("div",{"class":"css-y4udm8"})]
    all_descriptions.extend(descriptions)


# In[135]:


all_descriptions


# In[136]:


my_dic={}
my_dic['title']=all_titles
my_dic['link']=all_links
my_dic['location']=all_locations
my_dic['occupation']=all_occupations
my_dic['description']=all_descriptions
my_dic


# In[137]:


import pandas as pd
df=pd.DataFrame(my_dic)
df


# ### "data analysis" jobs scraping in Egypt

# In[138]:


urls=[]
urls+= [f"https://wuzzuf.net/search/jobs/?a=navbg&q=data%20analysis%20jobs%20in%20egypt&start={i}"for i in range(0,5)]
urls


# In[139]:


for url in urls :
    response=requests.get(url)
response


# In[140]:


all_titles=[]
for url in urls :
    soup=BeautifulSoup(response.content,"lxml")
    titles=[title.text for title in soup.find_all("h2",{"class":"css-m604qf"})]
    all_titles.extend(titles)


# In[141]:


soup


# In[142]:


all_titles


# In[143]:


all_links=[]
for url in urls:
    soup=BeautifulSoup(response.content,"lxml")
    links=[link.a["href"] for link in soup.find_all("h2",{"class":"css-m604qf"})]
    all_links.extend(links)


# In[144]:


all_links


# In[145]:


all_locations=[]
for url in urls:
    locations=[location.text for location in soup.find_all("div",{"class":"css-d7j1kk"})]
    all_locations.extend(locations)


# In[146]:


all_locations


# In[147]:


all_occupations=[]
for url in urls:
    occupations=[occupation.text for occupation in soup.find_all("div",{"class":"css-1lh32fc"})]
    all_occupations.extend(occupations)


# In[148]:


all_occupations


# In[149]:


all_descriptions=[]
for url in urls:
    descriptions=[description.text for description in soup.find_all("div",{"class":"css-y4udm8"})]
    all_descriptions.extend(descriptions)


# In[150]:


all_descriptions


# In[151]:


my_dic={}
my_dic['title']=all_titles
my_dic['link']=all_links
my_dic['location']=all_locations
my_dic['occupation']=all_occupations
my_dic['description']=all_descriptions
my_dic


# In[152]:


import pandas as pd
df_2=pd.DataFrame(my_dic)
df_2


# ### "data science" jobs scraping in Egypt

# In[159]:


urls=[]
urls+= [f"https://wuzzuf.net/search/jobs/?a=navbg&q=data%20science%20jobs%20in%20egypt&start={i}"for i in range(0,5)]
urls


# In[160]:


for url in urls :
    response=requests.get(url)
response


# In[161]:


all_titles=[]
for url in urls :
    soup=BeautifulSoup(response.content,"lxml")
    titles=[title.text for title in soup.find_all("h2",{"class":"css-m604qf"})]
    all_titles.extend(titles)


# In[162]:


all_titles


# In[163]:


all_links=[]
for url in urls:
    links = [link.a["href"] for link in soup.find_all("h2", {"class": "css-m604qf"})]
    all_links.extend(links)


# In[164]:


all_links


# In[165]:


all_locations=[]
for url in urls:
    locations=[location.text for location in soup.find_all("div",{"class":"css-d7j1kk"})]
    all_locations.extend(locations)


# In[166]:


all_locations


# In[167]:


all_occupations=[]
for url in urls:
    occupations=[occupation.text for occupation in soup.find_all("div",{"class":"css-1lh32fc"})]
    all_occupations.extend(occupations)


# In[168]:


all_occupations


# In[169]:


all_descriptions=[]
for url in urls:
    descriptions=[description.text for description in soup.find_all("div",{"class":"css-y4udm8"})]
    all_descriptions.extend(descriptions)


# In[170]:


all_descriptions


# In[171]:


my_dic={}
my_dic['title']=all_titles
my_dic['link']=all_links
my_dic['location']=all_locations
my_dic['occupation']=all_occupations
my_dic['description']=all_descriptions
my_dic


# In[173]:


import pandas as pd
df_3=pd.DataFrame(my_dic)
df_3


# ### "business intelligence" jobs scraping in Egypt

# In[175]:


urls=[]
urls+= [f"https://wuzzuf.net/search/jobs/?a=navbg&q=business%20intelligence%20jobs%20in%20egypt&start={i}"for i in range(0,5)]
urls


# In[176]:


for url in urls :
    response=requests.get(url)
response


# In[177]:


all_titles=[]
for url in urls :
    soup=BeautifulSoup(response.content,"lxml")
    titles=[title.text for title in soup.find_all("h2",{"class":"css-m604qf"})]
    all_titles.extend(titles)


# In[178]:


all_titles


# In[179]:


all_links=[]
for url in urls:
    links = [link.a["href"] for link in soup.find_all("h2", {"class": "css-m604qf"})]
    all_links.extend(links)


# In[180]:


all_links


# In[181]:


all_locations=[]
for url in urls:
    locations=[location.text for location in soup.find_all("div",{"class":"css-d7j1kk"})]
    all_locations.extend(locations)


# In[182]:


all_locations


# In[183]:


all_occupations=[]
for url in urls:
    occupations=[occupation.text for occupation in soup.find_all("div",{"class":"css-1lh32fc"})]
    all_occupations.extend(occupations)


# In[184]:


all_occupations


# In[185]:


all_descriptions=[]
for url in urls:
    descriptions=[description.text for description in soup.find_all("div",{"class":"css-y4udm8"})]
    all_descriptions.extend(descriptions)


# In[186]:


all_descriptions


# In[187]:


my_dic={}
my_dic['title']=all_titles
my_dic['link']=all_links
my_dic['location']=all_locations
my_dic['occupation']=all_occupations
my_dic['description']=all_descriptions
my_dic


# In[188]:


import pandas as pd
df_4=pd.DataFrame(my_dic)
df_4


# In[190]:


with pd.ExcelWriter(r"C:\Users\lenovo\Desktop\Page.xlsx") as m:
    df.to_excel(m, sheet_name='Sheet1',index=False)
    df_2.to_excel(m, sheet_name='Sheet2',index=False)
    df_3.to_excel(m, sheet_name='Sheet3',index=False)
    df_4.to_excel(m, sheet_name='Sheet4',index=False)


# In[ ]:




