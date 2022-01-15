class __Tower(object):
    
    def __init__(self) -> _Tower:
        self.damage = 1
        self.attack_speed = 1 # in shoots per second
        
    def deploy(self, x=0, y=0) -> None:
        self.x = x
        self.y = y
    
    def shot(self, target):
        target.hit(self.damage)


class BaseTower(__Tower):
    pass

# Here will be new towers classes