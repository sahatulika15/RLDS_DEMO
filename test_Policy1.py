"""
Usage :
python test_Policy.py ./save/filename (episodes)
this command will load the model and run for 10 experiments
"""
from DQN1 import DQNAgent
import numpy as np
import pickle
import sys
import env1
#from SVM_test1 import *
import random
import time
import matplotlib.pyplot as plt
from functions1 import one_hot_encoding

if len(sys.argv) > 1:
    # the filename has been given
    filename = sys.argv[1]  # contains the fielname
    """
    	if 'save' in filename:
        # the file contains the whole path
        pass
    else:
        filename = "./save/" + filename
	"""

else:
    filename = './save/final.h5'
print("Loading File {}".format(filename))
eps = None
if len(sys.argv) > 2:
    eps = sys.argv[2]  # the number of episodes to run for
time.sleep(1)
d = env1.DialougeSimulation()
# state_size = d.state_size
action_size = d.actions
state_size = d.state_size
agent = DQNAgent(state_size, action_size, hiddenLayers=[75], dropout=0.0, activation='relu', loadname=filename,
                 saveIn=False, learningRate=0.05, discountFactor=0.7,
                 epsilon=0.01)  # epislon is zero as we are testing and hence no exploration

# print(agent.model.get_weights())
time.sleep(1)
TotalReward = 0
if eps is not None:
    Episodes = int(eps)
else:
    Episodes = 1
rewards = []
iteration=[]
agent.load(filename)


for e in range(Episodes):
    i=0
    state = d.reset()
    all_act = []
    for z in range(0, action_size):
        all_act.append(z)
    #print(all_act)
    done = False
    running_reward = 0
    # make the initial state
    l = len(state)
    stateOriginal = state.copy()
    state = np.reshape(state, [l])
    #state = np.append(state, np.zeros(action_size))
    #state = np.append(state, np.zeros(l))

    state = np.reshape(state, [1, len(state)])
    # print("\n\n\n\n")
    print(state)
    # time.sleep(0.5)

    while done == False:
        i = i + 1
        done = False
	#all_act=predict(state)
	print(all_act)
        action = agent.act(state, all_act)
        print("The action taken : ")
        print(action)
        next_state, reward, done = d.step(action[0])        
        next_stateOriginal = next_state.copy()
        #print("the Reward : " + str(reward))
        # l = len(next_state)
        next_state = np.reshape(next_state, [l])
        #next_state = np.append(next_state, one_hot_encoding(action_size, action))
        #next_state = np.append(next_state, stateOriginal)
        next_state = np.reshape(next_state, [1, state_size])
        print("next_state==============")
        print(next_state)
        print("i=" + str(i))
    	state = next_state
    	stateOriginal = next_stateOriginal.copy()
    # add the total reward
    	#rewards.append(reward)
	running_reward +=reward
    rewards.append(running_reward)
    iteration.append(i)
    #TotalReward += running_reward

#print("The average Reward is {}".format(TotalReward / Episodes))
#print("The average Dialogue length is {}".format(i / Episodes))
print(rewards)
#print(TotalReward)
print(iteration)
print(np.mean(rewards,axis=0))
print(np.std(rewards,axis=0))
print(np.mean(iteration,axis=0))
print(np.std(iteration,axis=0))
# plt.plot(range(len(rewards)),rewards)
# plt.show()
