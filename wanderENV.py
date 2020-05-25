class wanderEnv():
    def __init__(self):
        self.x=0
        self.y=0
        self.w=0
        self.allowed=[]
        self.actin_list=[]


    def step(self,action):
        if action == 0:
            n_pos=(self.x + 1,self.y)
            self.w+=2
        elif action == 1:
            n_pos = (self.x , self.y+ 1)
            self.w = self.w*2
        elif action == 2:
            n_pos = (self.x - 1, self.y)
            self.w -=2
        elif action==3:
            n_pos = (self.x , self.y - 1)
            self.w=self.w/2

        self.actin_list.append(((self.x, self.y), n_pos))
        self.x,self.y=n_pos
        allowed_actions = []
        x, y = n_pos
        if 0<=x+1 < 5 and not ((x+1, y), (x, y)) in self.actin_list and not ((x, y), ((x+1, y))) in self.actin_list:
            allowed_actions.append(0)
        if 0<=y+1 < 5 and not ((x, y+1), (x, y)) in self.actin_list and not ((x, y), ((x, y+1))) in self.actin_list:
            allowed_actions.append(1)
        if 0<=x-1 < 5 and not ((x-1, y), (x, y)) in self.actin_list and not ((x, y), ((x-1, y))) in self.actin_list:
            allowed_actions.append(2)
        if 0<=y-1 < 5 and not ((x, y-1), (x, y)) in self.actin_list and not ((x, y), ((x, y-1))) in self.actin_list:
            allowed_actions.append(3)
        if not allowed_actions:
            self.done=True
        if self.x==4 and self.y==4 and self.w==0:
            self.done=True
            self.reward=0
            print('----------------------')
            print(self.actin_list)

        return [(self.x,self.y), self.w,allowed_actions,self.reward,self.done]
    def reset(self):
        self.x = 2
        self.y = 0
        self.w=4
        self.actin_list=[((0,0),(1,0)),((1,0),(2,0))]
        self.done=False
        self.reward=-1
        allowed_actions=[0,1]
        return [(self.x, self.y), self.w, allowed_actions, self.reward, self.done]
