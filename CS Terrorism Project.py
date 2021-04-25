#!/usr/bin/env python
# coding: utf-8

# In[98]:


br = "\n"


# In[99]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pprint
import nltk
import folium
from wordcloud import WordCloud

import plotly.graph_objs as go 
import plotly as py
import plotly.express as px
from plotly.offline import init_notebook_mode,iplot,plot
init_notebook_mode(connected=True)


import descartes
import geopandas as gpd
from shapely.geometry import Point, Polygon


# In[100]:


p1 = ('/Users/maryyoussef/Desktop/GTD/Clean GTD/GTD_1970_1998_Clean.csv')
df1 = pd.read_csv(p1)

p2 = ('/Users/maryyoussef/Desktop/GTD/Clean GTD/GTD_1999_2011_Clean.csv')
df2 = pd.read_csv(p2)

p3 = ('/Users/maryyoussef/Desktop/GTD/Clean GTD/GTD_2012_2014_Clean.csv')
df3 = pd.read_csv(p3)

p4 = ('/Users/maryyoussef/Desktop/GTD/Clean GTD/GTD_2015_2017_Clean.csv')
df4 = pd.read_csv(p4)

p5 = ('/Users/maryyoussef/Desktop/GTD/Clean GTD/GTD_2018_2019_Clean.csv')
df5 = pd.read_csv(p5)


dfs = [df1, df2, df3, df4, df5]

df = pd.concat(dfs)


# In[101]:


colnames = list(df.columns)
#print(colnames)
df = df.replace(r'^\s*$', np.nan, regex=True)


# In[102]:


df = df[df['iyear'] >= 2000]
print(df.columns)


# In[103]:


#list(df.columns)


# In[104]:


# from nltk.stem import WordNetLemmatizer 
# from nltk.tokenize import sent_tokenize
# from nltk.tokenize import word_tokenize
# from nltk.corpus import wordnet
# from nltk.probability import FreqDist
# from nltk.corpus import stopwords
# from wordcloud import WordCloud


# def TextAnalysis(column):
#     # Putting all of column content to 1 string
    
#     df[column] = df[column].str.lower()
    
#     sentence = df[column].tolist()
#     sentence = str(sentence)

#     # Initializing punctuations string  
#     punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
  
#     # Removing punctuations in string 
#     # Using loop + punctuation string   
#     for ele in sentence:  
#         if ele in punc:  
#             sentence = sentence.replace(ele, "")     
    
#     # Tokenizing word to remove stop words
#     tokenized_word=word_tokenize(sentence)
   
#     # Remove stop words and adding nan and al from empty values and city name
#     stop_words=set(stopwords.words("english"))
#     stop_words.add('nan')
    
#     # Filtering sentence to remove stop words
#     filtered_sent=[]
#     for w in tokenized_word:
#         if w not in stop_words:
#             filtered_sent.append(w)
    
#     # Lemmatize with POS Tag --> https://www.machinelearningplus.com/nlp/lemmatization-examples-python/
#     def get_wordnet_pos(word):
#         """Map POS tag to first character lemmatize() accepts"""
#         tag = nltk.pos_tag([word])[0][1][0].upper()
#         tag_dict = {"J": wordnet.ADJ,
#                     "N": wordnet.NOUN,
#                     "V": wordnet.VERB,
#                     "R": wordnet.ADV}

#         return tag_dict.get(tag, wordnet.NOUN)

#     # Making filtered sentence single string to lemmatize
#     filtered_sent = ' '.join(filtered_sent)
    
#     # Init Lemmatizer
#     lemmatizer = WordNetLemmatizer()

#     # Lemmatize string with the appropriate POS tag
#     sentfinal = ([lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in nltk.word_tokenize(filtered_sent)])
#     #print(sentfinal)

#     # Print freq of words in final clean sentence
#     fdist = FreqDist(sentfinal)
    
#     # Making sentence a string from a list for word cloud
#     str_sentfinal = ' '.join(map(str, sentfinal))
     
#     #Printing top 5 most common words and freq.
#     #print(fdist.most_common(5))
    
#     fig1 = plt.figure()
    
#     # Plotting top 30 words
#     title = "Top Words in {} Column".format(column.capitalize())
#     fdist.plot(10, cumulative=False, title=title)
#     plt.title(title)
#     fdist_fig_name = str(column) + '_fdist.jpg'  
#     #fig1.savefig(fdist_fig_name, bbox_inches = "tight")

#     # if using a Jupyter notebook, include:
#     %matplotlib inline

#     wordcloud = WordCloud(width = 700, height = 700, 
#                     background_color ='white', 
#                     min_font_size = 10).generate(str_sentfinal) 

    
#     # plot the WordCloud image                        
#     plt.figure(figsize = (5, 5), facecolor = None) 
#     plt.imshow(wordcloud) 
#     plt.axis("off") 
#     plt.tight_layout(pad = 0) 
#     titlewc = "Word Cloud From {} Column".format(column.capitalize())
#     plt.title(titlewc)
#     wc_fig_name = str(column) + '_wordcloud.jpg'
#     #plt.savefig(wc_fig_name)
#     plt.show()
    
    
# #motive, target1, scite1, propcomment
# TextAnalysis('motive')
# # TextAnalysis('target1')
# # TextAnalysis('scite1')
# # TextAnalysis('propcomment')


# In[105]:


# findword = 'claimed'
# numwords = 50
# claimed = []

# # Making entire column single string to analyze
# summs = df['motive'].tolist()
# summs = str(summs)

# # Printing numwords words before and after word claimed if found
# for i in summs.split('\n'):
#     z = i.split(' ')

#     for x in [x for (x, y) in enumerate(z) if findword in y]:
#         claimed.append(' '.join(z[max(x-numwords,0):x+numwords+1]))
        
# #pprint.pprint(claimed)

# however = []
# other = []
# howev = 'however'

# #If word has claimed, looking into which attacks had 'no group'

# for i in claimed: 
#     if howev in i:
#         however.append(i)
#     else:
#         other.append(i)

# #pprint.pprint(however)


# In[106]:


# Renaming district names according to loaded data frame

df['country'] = df['country'].replace(['United States'], 'USA-states')


# In[107]:


# fig3 = plt.figure()
# df.hist(figsize=(40,30))
# plt.show()


# In[108]:


fig, ax = plt.subplots(figsize=(12, 6))
ax.hist(x = df['iyear'])
plt.title('Distribution of Attacks by Year')
plt.xlabel("Year")
plt.ylabel("Count")
#plt.savefig('DistYear.jpg')

fig, ax = plt.subplots(figsize=(12, 6))
ax.hist(x = df['imonth'])
plt.title('Distribution of Attacks by Month')
plt.xlabel("Month")
plt.ylabel("Count")
#plt.savefig('DistMonths.jpg')


fig, ax = plt.subplots(figsize=(12, 6))
ax.hist(x = df['iday'])
plt.title('Distribution of Attacks by Day')
plt.xlabel("Day")
plt.ylabel("Count")
#plt.savefig('DistDay.jpg')

jan = df[df['imonth'] == 1]
dec = df[df['imonth'] == 12]

fig, ax = plt.subplots(figsize=(12, 6))
ax.hist(x = dec['iday'])
plt.title('Distribution of Days of Attacks in December')
plt.xlabel("Date of the Month")
plt.xticks(np.arange(0, 32))
plt.ylabel("Count")
ax.set_xlim(xmin=0, xmax=32, )
# #plt.savefig('DistDaysAttacksDec.jpg')


fig, ax = plt.subplots(figsize=(12, 6))
ax.hist(x = jan['iday'])
plt.title('Distribution of Days of Attacks in January')
plt.xlabel("Date of the Month")
plt.xticks(np.arange(0, 32))
plt.ylabel("Count")
ax.set_xlim(xmin=0, xmax=32, )
# #plt.savefig('DistDaysAttacksJan.jpg')


# In[109]:


rans = df[(df['ransompaid'] > 0) | (df['ransompaidus'] > 0) ]
#pd.set_option("display.max_colwidth", -1)  # to view all data in row

rans2 = rans[['motive', 'ransomamt', 'ransompaid']]
rans2.head()

pd.reset_option('^display.', silent=True)    # to reset setting back to condensed df view


# In[110]:


attack = df['attacktype1_txt'].value_counts()
attack = attack.to_dict()


fig = plt.figure(figsize=(24, 6))
plt.bar(x = attack.keys(), height = attack.values(), )
plt.title('Frequency of Attack Types')
plt.xlabel("Attack Type")
plt.ylabel("Count")
# plt.savefig('FreqAttacks.jpg')

# compclaim = df['claimmode_txt'].value_counts()
# compclaim = compclaim.to_dict()


# fig = plt.figure(figsize=(24, 6))
# plt.bar(x = compclaim.keys(), height = compclaim.values(), )
# plt.title('Count of Claim Responsibility')
# plt.xlabel("Claim Mode")
# plt.ylabel("Count")
# plt.savefig('ClaimMode.jpg')


# In[111]:


#print(colnames)


# In[112]:


df['nkill'] = df['nkill'].fillna(-1)
#print(set(df['nkill']))

df_plot = df[df['nkill'] > 0]
print(len(df_plot))
df_plot = df_plot[df_plot['nwound'].notna()]
print(len(df_plot))


# In[126]:


df_plot_top = df_plot.nlargest(4000,'nkill')


# In[128]:


get_ipython().run_line_magic('matplotlib', 'inline')

fig = px.scatter_mapbox(df_plot_top, lat="latitude", lon="longitude",zoom=3, height=300, 
                         color='iyear', size = "nkill", color_continuous_scale= 'Rainbow',
                         custom_data = ['country_txt', 'iyear', 'gname', 'nkill', 'nwound', 'targtype1_txt'])

fig.update_traces(
    hovertemplate="<br>".join([
        "City: %{customdata[0]}",
        "Year: %{customdata[1]}",
        "Group Name: %{customdata[2]}",
        "Killed: %{customdata[3]}",
        "Wounded: %{customdata[4]}",
        "Target Type: %{customdata[5]}"
            ]))


fig.update_layout(
    # add a title text for the plot
    title_text = 'Attack Types of Incidents Across the Globe with Magnitude of Nkilled',

    mapbox_style="white-bg",
    mapbox_layers=[
        {   "below": 'traces',
            "sourcetype": "raster",
            "sourceattribution": "United States Geological Survey",
            "source": [
                "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                ]
            }
          ])
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

fig.show()

import chart_studio

#    *~*~*~*~*~*~*~*~*~**~*~*~*~*~ ### KEEP THIS ###  *~*~*~*~*~*~*~*~*~**~*~*~*~*~*~*~*~*~*~*~*~*~*~**~*~*~*~*~

# username = 'mry8ea' # your username
# api_key = 'QPR3L9tJz8eTSJkuvdzN' # your api key - go to profile > settings > regenerate key
# chart_studio.tools.set_credentials_file(username=username, api_key=api_key)

# import chart_studio.plotly as py
# py.plot(fig, filename = 'CS5010 GTD Project', auto_open=True)


# In[113]:


get_ipython().run_line_magic('matplotlib', 'inline')

fig = px.scatter_mapbox(df_plot, lat="latitude", lon="longitude",zoom=3, height=300, 
                         color='iyear', size = "nkill", color_continuous_scale= 'Rainbow',
                         custom_data = ['country_txt', 'iyear', 'gname', 'nkill', 'nwound', 'targtype1_txt'])

fig.update_traces(
    hovertemplate="<br>".join([
        "City: %{customdata[0]}",
        "Year: %{customdata[1]}",
        "Group Name: %{customdata[2]}",
        "Killed: %{customdata[3]}",
        "Wounded: %{customdata[4]}",
        "Target Type: %{customdata[5]}"
            ]))


fig.update_layout(
    # add a title text for the plot
    title_text = 'Attack Types of Incidents Across the Globe with Magnitude of Nkilled',

    mapbox_style="white-bg",
    mapbox_layers=[
        {   "below": 'traces',
            "sourcetype": "raster",
            "sourceattribution": "United States Geological Survey",
            "source": [
                "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                ]
            }
          ])
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

fig.show()

import chart_studio

#    *~*~*~*~*~*~*~*~*~**~*~*~*~*~ ### KEEP THIS ###  *~*~*~*~*~*~*~*~*~**~*~*~*~*~*~*~*~*~*~*~*~*~*~**~*~*~*~*~

# username = 'mry8ea' # your username
# api_key = 'QPR3L9tJz8eTSJkuvdzN' # your api key - go to profile > settings > regenerate key
# chart_studio.tools.set_credentials_file(username=username, api_key=api_key)

# import chart_studio.plotly as py
# py.plot(fig, filename = 'CS5010 GTD Project', auto_open=True)


# In[114]:




#nwound_iyear = df.groupby('iyear')['nwound'].sum()

# df['nkill_iyear'] = df['iyear'].map(nkill_iyear)
# df['nwound_iyear'] = df['iyear'].map(nwound_iyear)


nkill_iyear_country = df.groupby(['iyear', 'country_txt'])['nkill'].sum()
nkill_iyear_country = nkill_iyear_country.reset_index()
nkill_iyear_country.head()


# In[115]:


nkill_iyear_country = df.groupby(['iyear', 'country_txt'])['nkill'].sum()
nkill_iyear_country = nkill_iyear_country.reset_index()
#nkill_iyear_country.head()

# #    *~*~*~*~*~*~*~*~*~**~*~*~*~*~ ### KEEP THIS ###  *~*~*~*~*~*~*~*~*~**~*~*~*~*~*~*~*~*~*~*~*~*~*~**~*~*~*~*~

max_nkill = nkill_iyear_country.nkill.max()
#print(max_nkill)

import plotly.express as px
gapminder = px.data.gapminder()
fig = px.choropleth(nkill_iyear_country,               
              locations="country_txt",
              locationmode = "country names",             
              color="nkill",
              hover_name="country_txt",  
              animation_frame="iyear"  ,     
              color_continuous_scale='Rainbow',  
              height=600 ,
                range_color= (0, max_nkill))   

fig.update_layout(
    # add a title text for the plot
    title_text = 'Number Killed by Terrorist Acts')


fig.show()

# #    *~*~*~*~*~*~*~*~*~**~*~*~*~*~ ### KEEP THIS ###  *~*~*~*~*~*~*~*~*~**~*~*~*~*~*~*~*~*~*~*~*~*~*~**~*~*~*~*~


# In[129]:


from nltk.stem import WordNetLemmatizer 
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from wordcloud import WordCloud


def TextAnalysis(column):
    # Putting all of column content to 1 string
    
    df[column] = df[column].str.lower()
    
    sentence = df[column].tolist()
    sentence = str(sentence)

    # Initializing punctuations string  
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
  
    # Removing punctuations in string 
    # Using loop + punctuation string   
    for ele in sentence:  
        if ele in punc:  
            sentence = sentence.replace(ele, "")     
    
    # Tokenizing word to remove stop words
    tokenized_word=word_tokenize(sentence)
   
    # Remove stop words and adding nan and al from empty values and city name
    stop_words=set(stopwords.words("english"))
    stop_words.add('nan')
    
    # Filtering sentence to remove stop words
    filtered_sent=[]
    for w in tokenized_word:
        if w not in stop_words:
            filtered_sent.append(w)
    
    # Lemmatize with POS Tag --> https://www.machinelearningplus.com/nlp/lemmatization-examples-python/
    def get_wordnet_pos(word):
        """Map POS tag to first character lemmatize() accepts"""
        tag = nltk.pos_tag([word])[0][1][0].upper()
        tag_dict = {"J": wordnet.ADJ,
                    "N": wordnet.NOUN,
                    "V": wordnet.VERB,
                    "R": wordnet.ADV}

        return tag_dict.get(tag, wordnet.NOUN)

    # Making filtered sentence single string to lemmatize
    filtered_sent = ' '.join(filtered_sent)
    
    # Init Lemmatizer
    lemmatizer = WordNetLemmatizer()

    # Lemmatize string with the appropriate POS tag
    sentfinal = ([lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in nltk.word_tokenize(filtered_sent)])
    #print(sentfinal)

    # Print freq of words in final clean sentence
    fdist = FreqDist(sentfinal)
    
    # Making sentence a string from a list for word cloud
    str_sentfinal = ' '.join(map(str, sentfinal))
     
    #Printing top 5 most common words and freq.
    #print(fdist.most_common(5))
    
    fig1 = plt.figure()
    
    # Plotting top 30 words
    title = "Top Words in {} Column".format(column.capitalize())
    fdist.plot(10, cumulative=False, title=title)
    plt.title(title)
    fdist_fig_name = str(column) + '_fdist.jpg'  
    #fig1.savefig(fdist_fig_name, bbox_inches = "tight")

    # if using a Jupyter notebook, include:
    get_ipython().run_line_magic('matplotlib', 'inline')

    wordcloud = WordCloud(width = 700, height = 700, 
                    background_color ='white', 
                    min_font_size = 10).generate(str_sentfinal) 

    
    # plot the WordCloud image                        
    plt.figure(figsize = (5, 5), facecolor = None) 
    plt.imshow(wordcloud) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 
    titlewc = "Word Cloud From {} Column".format(column.capitalize())
    plt.title(titlewc)
    wc_fig_name = str(column) + '_wordcloud.jpg'
    #plt.savefig(wc_fig_name)
    plt.show()
    
    
#motive, target1, scite1, propcomment
TextAnalysis('motive')
# TextAnalysis('target1')
# TextAnalysis('scite1')
# TextAnalysis('propcomment')


# In[ ]:


findword = 'claimed'
numwords = 50
claimed = []

# Making entire column single string to analyze
summs = df['motive'].tolist()
summs = str(summs)

# Printing numwords words before and after word claimed if found
for i in summs.split('\n'):
    z = i.split(' ')

    for x in [x for (x, y) in enumerate(z) if findword in y]:
        claimed.append(' '.join(z[max(x-numwords,0):x+numwords+1]))
        
#pprint.pprint(claimed)

however = []
other = []
howev = 'motive'

#If word has claimed, looking into which attacks had 'no group'

for i in claimed: 
    if howev in i:
        however.append(i)
    else:
        other.append(i)

pprint.pprint(however)

