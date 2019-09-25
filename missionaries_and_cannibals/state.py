import operator


class State:
    def __init__(self, state, action):
        self.state = state
        self.action = action

    def move(self):
        pass
                

    def isActionValid(self):
        if self.state[2] != self.action[2]:
            return False
        elif self.state[0] < self.state[1]:
            return False
        elif (self.action[0] + self.action[1] >= 2 | | self.action[0]+self.action[1] == 0):
            return False
