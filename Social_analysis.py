#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


# In[48]:


edgelist = pd.read_excel('D://Uchyoba_gumanitaristika//diplom//Сетевой анализ//Богоявленский(1880-1919)edges.xlsx')
nodelist = pd.read_excel('D://Uchyoba_gumanitaristika//diplom//Сетевой анализ//Богоявленский(1880-1919)nodes.xlsx')


# print(edgelist.head())
# print(nodelist.head())

# In[49]:


print(edgelist.head()) 
print(nodelist.head())


# In[52]:


g = nx.Graph()


# In[53]:


for i, elrow in edgelist.iterrows():
    g.add_edge(elrow[1], elrow[4], relation=elrow[2])


# In[56]:


for i, nlrow in nodelist.iterrows():
    g.add_node(nlrow['Name'] == nlrow['Type'])


# In[57]:


print(nx.info(g))


# In[60]:


pos = nx.spring_layout(g)
betCent = nx.betweenness_centrality(g, normalized=True, endpoints=True)
node_color = [20000.0 * g.degree(v) for v in g]
node_size =  [v * 10000 for v in betCent.values()]
plt.figure(figsize=(20,20))
nx.draw_networkx(g, pos=pos, with_labels=False,
                 node_color=node_color,
                 node_size=node_size )
plt.axis('off')
plt.savefig('network')


# In[61]:


sorted(betCent, key=betCent.get, reverse=True)[:15]


# In[64]:


pos = nx.spring_layout(g)
betCent = nx.degree_centrality(g)
node_color = [20000.0 * g.degree(v) for v in g]
node_size =  [v * 10000 for v in betCent.values()]
plt.figure(figsize=(20,20))
nx.draw_networkx(g, pos=pos, with_labels=False,
                 node_color=node_color,
                 node_size=node_size )
plt.axis('off')
plt.savefig('network_degree')


# In[65]:


sorted(betCent, key=betCent.get, reverse=True)[:15]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




