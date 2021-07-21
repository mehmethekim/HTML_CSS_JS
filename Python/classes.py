class Point():
    def __init__(self,inp1,inp2):
        self.x = inp1
        self.y = inp2
        self.z = self.y
p = Point(2,10)
print(p.x)
print(p.y)
print(p.z)
