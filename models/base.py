import torch
import torch.nn as nn
import torch.nn.functional as F

class Base(nn.Module):
    def __init__(self, size):
        super(Base, self).__init__()
        self.size = size
        self.fc1 = nn.Linear(size, size)
        self.fc2 = nn.Linear(size, size)
        self.fc3 = nn.Linear(size, size)
    
    def _call(self, x):
        self.out = F.relu(self.fc1(x))
        self.out = F.relu(self.fc2(x))
        self.out = F.relu(self.fc3(x))
        return self.out
    
    def getOutSize(self):
        return self.size