class Spaceship:
    tractor_beam = 'Off'
    
    def __init__(self , name , kind):
        self.name = name 
        self.kind = kind
        self.speed = None
        
    def warp(self , warp):
        self.speed = warp
        print(f"Warp {warp} , engage!")
    def tractor(self):
        if self.tractor_beam == 'Off':
            self.tractor_beam = 'On'
            print('Tractor beam on....')
        else:
            self.tractor_beam = 'Off'
            print('Off...')
Space = Spaceship('Hridu' , "Rocket")
Space.warp(200)
Space.tractor()
print(Space.tractor_beam)