#this is state to likely nextstate model
#the model update for 
#coding utf-8
from base import Base

class STT(Base):
    def __init__(self, size):
        super(STT, self).__init__(size)
    
    def forward(self, x):
        return self._call(x)