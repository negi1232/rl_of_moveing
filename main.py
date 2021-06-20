from typing import Pattern
import networkx as nx
from matplotlib import pyplot as plt 
import random
import os

import numpy as np
np.random.seed(seed=32)#テストのためシード値を固定
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def createnetwork():
    G = nx.Graph()
    G.add_nodes_from(['s0','s1','s2','s3','s4','s5','s6','s7','s8','s9','s10','s11','s12','s13','s14','s15'])
    G.add_edges_from([('s0','s1')])
    G.add_edges_from([('s1','s2'),('s1','s5')])
    G.add_edges_from([('s2','s3')])
    G.add_edges_from([('s3','s7')])
    G.add_edges_from([('s4','s5'),('s4','s8')])
    G.add_edges_from([('s5','s6')])
    G.add_edges_from([('s6','s7')])
    G.add_edges_from([('s7','s11')])
    G.add_edges_from([('s8','s9'),('s8','s12')])
    G.add_edges_from([('s9','s10')])
    G.add_edges_from([('s10','s11'),('s10','s14')])
    G.add_edges_from([('s11','s15')])
    G.add_edges_from([('s12','s13')])
    G.add_edges_from([('s13','s14')])
    return G
def createreward(G):
    mydict=dict()
    rewardsum=100
    arr = np.random.rand(1, len(G))
    arr=arr*rewardsum / arr.sum()
    count=0
    for i in G:
        mydict[i]=arr[0][count]
        count+=1

    return mydict

def createpolicy(G):
    mydict=dict()
    for i in G:
        reward=list()
        a=int(100/(G.degree(i)+1))
        for j in range(G.degree(i)+1):
            reward.append(a)
        pattern=list(nx.all_neighbors(G, i))
        pattern.insert(0, i)
        mydict[i] = [G.degree(i),pattern,reward]

    return mydict

    
if __name__ == '__main__':
    step=60#60回の移動で最も累積報酬の高いルートを探す
    G=createnetwork()#mapに見立てたnetworkを生成
    policy=createpolicy(G)#ネットワークからポリシーを生成
    reward=createreward(G)#総和が100のそれぞれのノードに対する報酬を生成


    nx.draw (G)
    plt.show()
    print("end")