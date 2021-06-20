import random

import numpy as np
from matplotlib import pyplot as plt

class ValueIteration:
    def __init__(self, n_states, n_actions, probs):
        self.n_states = n_states
        self.n_actions = n_actions
        self.probs = probs

    def __call__(self, gamma, epslion, reward_function=None):
        probs = self.probs
        n_states = self.n_states#16
        n_actions = self.n_actions#4
        V = np.zeros(n_states)#今回は、16行1列で初期化
        
        def compute_action_value(state):
            A = np.zeros(self.n_actions)#今回は、4行1列で初期化
            for action in range(n_actions):#4回for分を回す
                for prob, next_state, reward, done in probs[state][action]:#現在地点から起こせるアクションの辞書型を参照し代入forを使う理由は一括で代入できるから。
                    reward = reward if reward_function is None else reward_function(state)#reward_functionが入力されていなければ、rewardを代入,あればreward_function(state)を実行　
                    if reward !=0:
                        pass
                        print(reward)
                        print("reward isnot 0")
                    A[action] += prob * (reward + gamma * V[next_state])#A[action] 現在地点stateから起こせる行動ごとに　： probは基本１なぜなら進めないことはないから　：　reward 行動を起こした時得られる報酬 :gamma 割引率 : 次の行動をした時に得られる報酬
            return A
        
        xlim = [0, 10]
        ylim = [0, 1]
        X, Y = [0], [0]

        while True:#状態価値関数Vを更新しdelta < epslionなるまで繰り返す
            delta = 0#すべての状態に対して計算するため毎回初期化する
            for state in range(n_states):#16回for分を回す(すべてのマスに対して処理をするため)
                A = compute_action_value(state)#今いる地点stateからほかのマスに移動する
                best_action_value = A.max()#求めたAの最大値を代入
                delta = max(delta, np.abs(best_action_value - V[state]))#今までの値deltaと今回の値np.abs...を比較し、より大きいほうを代入
                V[state] = best_action_value#今の状態の状態価値関数V(s)を更新
            
            Y.append(delta)
            X.append(len(Y))
            if len(X) > 10:
                 xlim[0] += 1
                 xlim[1] += 1
            #     ylim[0] = min(Y[-50:])
            #     ylim[1] =  max(Y[-50:])
            plt.ylim(ylim[0], ylim[1])    
            plt.xlim(xlim[0], xlim[1])
            plt.plot(X, Y)
            plt.pause(0.0001)
            if delta < epslion:#epslionは1e-05(0.00001)
                break

        policy = np.zeros([n_states, n_actions])
        for state in range(n_states):
            A = compute_action_value(state)
            policy[state] = A

        policy -= policy.max(axis=1, keepdims=True)
        max_values = np.broadcast_to(policy.max(axis=1, keepdims=True), policy.shape)
        policy = np.where(policy == max_values, policy, np.NINF)
        policy = np.exp(policy) / np.exp(policy).sum(axis=1, keepdims=True)
        return V, policy