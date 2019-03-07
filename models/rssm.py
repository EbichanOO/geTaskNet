#this is env-data to nextstate model
#coding utf-8
import torch
from base import Base
class RSSM(Base):
    def __init__(self, size):
        super(RSSM, self).__init__(size)
        self.reserve = torch.zeros(size,)
    
    def getReserve(self):
        return self.reserve
    
    def forward(self, x):
        # input is torch variable.
        # not numpy since this rnn get other model's output.
        x = x + self.reserve
        out = self._call(x)
        self.reserve = out
        return out