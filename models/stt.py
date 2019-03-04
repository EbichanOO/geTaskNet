#this is state to task model
#the model update for 
#coding utf-8
import torch
import torch.nn as nn
import torch.nn.functional as F

class STT(nn.Module):
    def __init__(self, insize):
        super(STT, self).__init__()
        self.size = insize
        self.fc1 = nn.Linear(self.size, self.size)
        self.fc2 = nn.Linear(self.size, self.size)
        self.fc3 = nn.Linear(self.size, self.size)
    
    def reloss(self, opt):
        loss = F.
    
    def forward(self, x):
        tmp = F.relu(self.fc1(x))
        tmp = F.relu(self.fc2(x))
        return F.relu(self.fc3(x))
