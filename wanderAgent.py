from wanderENV import wanderEnv
import random
import numpy as np 

# table setting
LEARNING_RATE = 0.1
DISCOUNT = 0.95
EPISODES = 100000
SHOW_EVERY=1000

env= wanderEnv()

q_table= np.random.uniform(low=-2, high=0, size=(5,5,4))

for episode in range(1,EPISODES):
    
    pos, w, allowed, reward, done=env.reset()
    while not done:
        action=random.choice(allowed)
        pos,w,allowed,reward,done =env.step(action)
        if episode%SHOW_EVERY==0:
            print(pos, w, allowed, reward, done)
        if not done:
            current_q=q_table[pos+(action,)]
            for i in range(4):
                if not i in allowed:
                    q_table[pos+(i,)]= -2
            max_future_q= np.max(q_table[pos])
            new_q=(1-LEARNING_RATE) * current_q +LEARNING_RATE*((0-w)+DISCOUNT*max_future_q)
            q_table[pos+(action,)]= new_q
        elif pos==(4,4) and w==0:
            q_table[pos+(action,)]=0





