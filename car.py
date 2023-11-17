class car :
    def __init__ (self,speed,color,nitrospeed,model) :
        self.speed=speed
        self.color=color
        self.nitrospeed=nitrospeed
        self.model=model
    def turn(self):
        print(self.model , "turn")
    def accelarate(self):
        print(self.model , "accelarate")
    def brake(self):
        print(self.model , "brake")
    def boost(self):
        print(self.model , "boost")