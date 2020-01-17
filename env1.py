# -*- coding: utf-8 -*-


import numpy as np
import random
from functions1 import *


class DialougeSimulation(object):
    """
    State Descipriton:
    State: contains 6 variables (greet, deptCity, arrCity, deptTime, depDay, class ,number of iteration uptil no)
     Action Set :
     greet (0), ask{arrCity,deptCity,deptTime,depDay,class}()
     reask/confirm{arrCity,deptCity,deptTime,depDay,class} .
     askDeptandArr, askDateTime # hybrid actions

    # adding a seveth parameter for number of iterations
    """

    # @1/3/18 changing the default weight value of w2 to 8 and w3 to 13
    def __init__(self, w1=1, w2=8, w3=13):
        """
        The weights are as follows
        w1 : is the interaction weigt
        w2 : is the change in confidence value
        w3: is the weight given to weight value
        """
        self.state_size = 5
        self.actions = 13
        self.current_state = []  # the current state of the agent
        self.states = np.zeros([0, 5])  # this is the collection of all the states
        self.init_state()
        self.num_iter = 0
        # self.actions = ['greet','askDeptCity','askArrCity','askDepDay','askDepTime','askClass','askDeptArrCity','askDateTIme','reaskDeptCity','reaskArrCity','reaskDepDay','reaskDepTime','reaskClass','closeConversation' ]
        self.w1 = w1  # interaction weight
        self.w2 = w2
        self.w3 = w3
        # 1/3/18 Keep a track of the actions taken i.e a count of number of action taken for each type
        self.actions_taken = np.zeros([self.actions])
        # @6/3/18 calculate the max possible value
        self.threshold = 0.7
        #self.max_reward = max(self.w3, self.w2 * 5 * self.threshold)

    def init_state(self):
        self.states = np.array([[0.0, 0.0, 0.0, 0.0, 0.0]])  # initliase with zero for all values
        self.current_state = self.states[-1]
        # 1/3/18 reinit the actions taken matrix
        self.actions_taken = np.zeros([self.actions])

    def random_init_state(self):
        self.states = np.array(
            [[random.random() for i in range(self.state_size)]])  # initialise with zero for all values
        self.current_state = self.states[-1]
        # 1/3/18 reinit the actions taken matrix
        self.actions_taken = np.zeros([self.actions])


    def check(self, action):
        self.threshold = 0.7
        if (self.threshold < self.current_state[action - 7 - 1]):
            return 1
        else:
            return 0

    def step(self, action):
        # this will be the next step to take for an action lies between 0 - 12 including both
        """
        Now the confidence value of the slots will be defined on the language unit of the system:
        We will assume the langugae system to be a random funciton generator which
        """
        done = False

        reward = 0
        # action is a numeric value

        new_state = np.array([float('%.4f' % elem) for elem in self.current_state])
        #if action == 0 and self.num_iter == 0:  # greeting should be first
            #new_state[0] = 1
        if action >= 0 and action <= 4:  # the action is to ask a slot value
            new_state[action] = 0.2 * random.random() + 0.55  # the confidenec value lies between 0.6 - 0.8
        if action > 6 and action <= 11:
            if new_state[action - 7] < 0.1:
                pass
            else:
                new_state[action - 7] = (1 - new_state[action - 7]) * 0.85 + new_state[
                    action - 7]  # @1/3/18 18:49:00the ask part has happned
        if action == 5:
            new_state[0] = 0.2 * random.random() + 0.55
            new_state[1] = 0.2 * random.random() + 0.55
        if action == 6:
            new_state[2] = 0.2 * random.random() + 0.55
            new_state[3] = 0.2 * random.random() + 0.55

        if action == 12:
            done = True
            val = soft_check_state(self.current_state)

            if (val>0):
                reward = val * (sum(self.current_state))*self.w2
                reward = abs(reward)
                print("r in if=" + str(reward))
            else:
                # @7/3/18 added w2 again
                reward = -self.w2*(sum(np.full(5, 1)) - sum(self.current_state))
        else:
            # @1/3/18 we have to update the self.w1 to be affected byt he action taken 
            print(new_state)
            print(self.current_state)
            # @7/3/18 added w2 again
            reward = self.w2*(sum(new_state) - sum(self.current_state))
            reward = reward - self.w1 
        noise_tobe_added = np.random.rand(len(self.current_state))*0.02 -0.01
        self.num_iter = self.num_iter + 1
        #new_state[6] = self.num_iter
        self.current_state = np.array([float('%.3f' % elem) for elem in new_state])

        self.states = np.append(self.states, [self.current_state], axis=0)
        reward = float(reward)#/self.max_reward

        return self.current_state, reward, done

    # need an indentifier to indetify the end of DialougeSimualtion
    def reset(self):
        """
        reset the state to the statrting poitn
        """
        i = random.random()
        if i < 0.5:
            self.init_state()
        else:
            self.random_init_state()
        self.num_iter = 0

        return self.current_state
