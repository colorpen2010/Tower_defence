import pygame, random


class generation():
    def __init__(self, backgrounds,background=None,types=0 ,xy=50):
        self.xy = xy
        self.type=types
        self.background = background
        self.backgrounds = backgrounds
        self.spisoc=[]
        self.pixels = 10


    def map_generation(self, dest=0, height=0):
        while height < 800:
            if dest <= 800:
                self.spisoc.append(self.background.blit(random.choice(self.backgrounds), [dest, height]))
                dest += self.xy
            elif height != 800:
                height += self.xy
                dest = 0

                pass

    def restart(self):
        self.x = 0
        self.y = 0
        self.spisoc.clear()


    def resize_randomizer(self):
        # return
        # self.xy=random.randint(1,100)
        self.pixels=random.randint(4,40)
    def resive(self, kva=None):
        if self.type==0:
            for o in self.backgrounds:
                self.xy = round(800 / self.pixels,0)
                kva.append(pygame.transform.scale(o, [self.xy, self.xy]))
            self.backgrounds.clear()
            for i in kva:
                self.backgrounds.append(i)
        if self.type==1:
            self.xy = round(800 / self.pixels, 0)
            self.backgrounds=pygame.transform.scale(self.backgrounds, [self.xy, self.xy])
            print(1)
