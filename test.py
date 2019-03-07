class TestA():
    def __init__(self, x):
        self.x = x
    
    def call(self, y):
        self.out = self.x + y
        return self.out

class TestB(TestA):
    def __init__(self, x):
        super(TestB, self).__init__(x)

actor = TestB(10)
print(actor.call(1))