import numpy as np
from utils import *
from env import *
from robot import *
from visualizer import Visualizer
import time

def calc_reward(env, inputs):
    # inputs are states that are traversed
    net_reward = 0
    for state in inputs:
        net_reward += state.reward
    return net_reward

if __name__ == '__main__':
    # Problem 2.1
    # rewards = range(W*L)

    # Problem 2.2
    rewards = [-100, -100, -100, -100, -100, -100,
    -100, 0, 0, -10, 1, -100,
    -100, 0, 0, -10, 0, -100,
    -100, 0, 0, 0, 0, -100,
    -100, 0, 0, 0, 0, -100,
    -100, -100, -100, -100, -100, -100
    ]
    gamma = 0.9

    robot = Robot(1, 4, 6, 0)
    env = Environment(W, L, rewards, robot)
    
    start = time.time()
    policy = env.get_init_policy()

    global opt_policy
    global opt_values
    start = time.time()
    opt_policy, opt_vals = env.alt_find_opt_policy(policy, gamma)
    print((time.time()-start)/1000, "Seconds")
    route = [(robot.x, robot.y, robot.heading)]

#    for i in range (6):
#        for j in range(6):
#            for k in range(12):
#                for i2 in range (6):
#                    for j2 in range(6):
#                        for k2 in range(12):
#                            for a in actions:
#                                if(env.get_p(env.stateAt(i,j,k), env.stateAt(i2,j2,k2), a) > 0):
#                                    print(((i,j,k), a, (i2,j2,k2), env.get_p(env.stateAt(i,j,k), env.stateAt(i2,j2,k2), a)))

    for i in range(10):
        action = opt_policy[env.robot.heading][env.robot.y][env.robot.x]
        print('action:', action)
        next_state = env.get_next_state(action)
        print('next_state: ', next_state)
        env.robot.move(next_state.x, next_state.y, next_state.heading)
        print('robot pos: ', env.robot.x, env.robot.y, env.robot.heading)
        route.append((env.robot.x, env.robot.y, env.robot.heading))

    vis = Visualizer(route)
    vis.showPolicy(opt_policy)

    # seq = [(robot.x, robot.y, robot.heading)]
    # for i in range(10):
    #     action = policy[env.robot.heading][env.robot.y][env.robot.x]
    #     # print('action:', action)
    #     next_state = env.get_next_state(action)
    #     # print('next_state: ', next_state)
    #     env.robot.move(next_state.x, next_state.y, next_state.heading)
    #     # print('robot pos: ', env.robot.x, env.robot.y, env.robot.heading)
    #     seq.append(( env.robot.x, env.robot.y, env.robot.heading))
    # vis = Visualizer(seq)
    # vis.show()
    

