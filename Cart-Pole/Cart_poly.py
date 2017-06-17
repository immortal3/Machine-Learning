import gym
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras import optimizers
from keras.models import load_model

env = gym.make('CartPole-v0')


classifier = Sequential()
def NN():
    classifier.add(Dense(output_dim=50,activation='relu',input_dim = 4))
    classifier.add(Dropout(p=0.5))
    classifier.add(Dense(output_dim=150,activation='relu'))
    classifier.add(Dropout(p=0.5))
    classifier.add(Dense(output_dim=250,activation='relu'))
    classifier.add(Dropout(p=0.5))
    classifier.add(Dense(output_dim=150,activation='relu'))
    classifier.add(Dropout(p=0.5))
    classifier.add(Dense(output_dim=100,activation='relu'))
    classifier.add(Dropout(p=0.5))
    classifier.add(Dense(output_dim=50,activation='relu'))
    classifier.add(Dropout(p=0.5))
    classifier.add(Dense(output_dim=1,activation='sigmoid'))
    sgd = optimizers.adam(lr=0.003)
    classifier.compile(optimizer=sgd,loss= 'MSE',metrics=['accuracy'])



def runoptimizer(x):
    x = np.load(x)
    X = np.array([i[0] for i in x]).reshape(-1,len(x[0][0]))
    y = [i[1] for i in x]
    classifier.fit(X,y,batch_size=32,nb_epoch=3)
    classifier.save('cart_pole.model')

def Training():
    numberOfEpisode = 10000
    goalPoint = 50
    data = []
    for i in range(numberOfEpisode):
        observation = env.reset()
        Total_reward = 0
        tempdata = []
        templabel = []
        prevobs = observation
        while True:
            #print (observation)
            #env.render()
            action = env.action_space.sample()
            obs , reward , done , info = env.step(action)
            tempdata.append(prevobs)
            templabel.append(action)
            prevobs = obs
            Total_reward += reward
            if done:
                if(Total_reward >= goalPoint):
                    for x,y in zip(tempdata,templabel):
                        data.append([x,y])
                break
    data = np.array(data)
    print (data)
    np.save('cart_pole_training_Data_new',data)




def Testing():
    classifier = load_model('cart_pole.model')
    numberOfPlay = 10
    max_reward = 0
    total_score = 0
    for i in range(numberOfPlay):
        obs = env.reset()
        Total_reward = 0
        while True:
            #print (observation)
            env.render()
            obs = np.expand_dims(obs,axis = 0)
            action = classifier.predict(obs)
            if(action >= 0.5):
                action = 1
            else:
                action = 0
            obs , reward , done , info = env.step(action)
            print (Total_reward)
            if(reward > 0):
                Total_reward += reward
                if(Total_reward>max_reward):
                    max_reward = Total_reward
            if done:
                total_score += Total_reward
                print ('died,Total_reward:', Total_reward)
                break
    print ('MaxReward:',max_reward,'avg:',total_score/numberOfPlay)


def buildModel():
    NN()
    Training()
    runoptimizer('cart_pole_training_Data_new.npy')
def TestModel():
    Testing()


#buildModel()
Testing()
