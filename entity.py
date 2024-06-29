import pygame,random

class generation():
    def __init__(self,background,backgrounds,xy=50):
        self.xy=xy
        self.background=background
        self.backgrounds=backgrounds
    def map_generation(self,dest=0,height=0):
        while height<=800:
            if dest<=800:
                self.background.blit(random.choice(self.backgrounds), [dest, height])
                dest +=self.xy
            elif height != 800:
                height += self.xy
                dest = 0

                pass
    def restart(self):
        self.x=0
        self.y=0
    def resize_randomizer(self):
        self.xy=random.randint(10,100)
    def resive(self,kva):
        for o in self.backgrounds:
            kva.append(pygame.transform.scale(o, [self.xy, self.xy]))
        self.backgrounds.clear()
        for i in kva:
            self.backgrounds.append(i)