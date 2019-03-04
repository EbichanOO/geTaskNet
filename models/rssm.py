#this is env-data to state model
#coding utf-8
import torch
import torch.nn as nn
import torch.nn.functional as F
class RSSM(nn.Module):
    def __init__(self, insize):
        super(RSSM, self).__init__()
        self.size = insize[0]
        self.fc1 = nn.Linear(self.size, self.size)
        self.fc2 = nn.Linear(self.size, self.size)
        self.fc3 = nn.Linear(self.size, self.size)
        self.reserve = torch.zeros(self.size,)
    
    def getOutSize(self):
        return self.size
    
    def getReserve(self):
        return self.reserve
    
    def forward(self, x):
        # input is torch variable.
        # not numpy since this rnn get other model's output.
        x = x + self.reserve
        tmp = F.relu(self.fc1(x))
        tmp = F.relu(self.fc2(x))
        tmp = F.relu(self.fc3(x))
        self.reserve = tmp
        return tmp