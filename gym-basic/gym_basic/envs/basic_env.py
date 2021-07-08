import gym

class BasicEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.action_space = gym.spaces.Discrete(2)
        self.observation_space = gym.spaces.Discrete(2)

    def step(self, action):
        state = 1
        prediction = action
        if action == 1:
            if prediction == 1:
                reward = 10
            else:
                reward = 0
        else:
            if prediction == 1:
                reward = 15
            else:
                reward = 5

        done = True

        info = {}

        return state, reward, done, info

    def reset(self):
        state = 0

        return state

    def render(self, mode='human'):
        pass

    def close(self):
        pass
