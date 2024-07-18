import pygame, random


class generation():
    def __init__(self, backgrounds,background=None,types=0 ,xy=50):
        self.xy=xy
        self.x = xy
        self.y=xy
        self.type=types
        self.background = background
        self.backgrounds = backgrounds
        self.spisoc=[]
        self.pixels = 10


    def map_generation(self, dest=0, height=0,):
        self.background.fill([0,0,0])
        while height < 800:
            if dest <= 800:
                self.spisoc.append(self.background.blit(random.choice(self.backgrounds), [dest, height]))
                dest += self.x
                self.y=self.x
            elif height != 800:
                height += self.x
                self.y=self.x
                dest = 0

                pass

    def map_regeneration(self,map,backgrounds):
        height=0
        dest=height
        while height < 800:
            for i in map:
                if i==0:
                    if dest <=800:
                        self.spisoc.append(self.backgrounds[0],dest,height)
                        dest+=self.x
                        self.y=self.x
                    elif height != 800:
                        height += self.x
                        self.y = self.x
                        dest = 0

                        pass
            print(i)

    def restart(self):
        self.x = self.xy
        self.y = self.xy
        self.spisoc.clear()


    def resize_randomizer(self):
        self.pixels = random.randint(4, 40)
        return self.pixels
    def resive(self,pixels=10, kva=None):
        self.pixels=pixels
        if self.type==0:
            for o in self.backgrounds:
                self.x = round(800 / self.pixels,0)
                self.y=self.x
                self.xy=self.x
                kva.append(pygame.transform.scale(o, [self.x, self.y]))
            self.backgrounds.clear()
            for i in kva:
                self.backgrounds.append(i)
        if self.type==1:
            self.x = round(800 / self.pixels, 0)
            self.y = self.backgrounds.get_height()*self.x/self.backgrounds.get_width()
            self.backgrounds=pygame.transform.scale(self.backgrounds, [self.x, self.y])
