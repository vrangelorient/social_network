#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


edgelist = pd.read_excel('edges.xlsx')
nodelist = pd.read_excel('nodes.xlsx')
# print(edgelist.head())
# print(nodelist.head())


g = nx.Graph()


for i, elrow in edgelist.iterrows():
    g.add_edge(elrow[1], elrow[4], relation=elrow[2])


for i, nlrow in nodelist.iterrows():
    g.add_node(nlrow['Name'] == nlrow['Type'])


print(nx.info(g))


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


sorted(betCent, key=betCent.get, reverse=True)[:15]


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


sorted(betCent, key=betCent.get, reverse=True)[:15]

