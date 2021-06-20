from typing import Pattern
import networkx as nx
from matplotlib import pyplot as plt 
import random
import os
from value_iteration import ValueIteration
import numpy as np
import preparation
np.random.seed(seed=32)#テストのためシード値を固定
os.chdir(os.path.dirname(os.path.abspath(__file__)))

    
if __name__ == '__main__':
    step=60#60回の移動で最も累積報酬の高いルートを探す
    G=preparation.createnetwork()#mapに見立てたnetworkを生成
    policy=preparation.createpolicy(G)#ネットワークからポリシーを生成
    reward=preparation.createreward(G)#総和が100のそれぞれのノードに対する報酬を生成


    nx.draw (G)
    plt.show()
    print("end")