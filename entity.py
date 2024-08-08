import pygame, random,image_worker


class generation():
    def __init__(self, backgrounds,backgrounds2=None,background=None,types=0 ,xy=50):
        self.xy=xy
        self.x = xy
        self.y=xy
        self.kartinka=backgrounds
        self.type=types
        self.zapreshenaia_kartinka = backgrounds2
        self.background = background
        self.backgrounds = backgrounds
        self.spisoc=[]
        self.pixels = 10
        self.grass_or_sand=[]


    def map_generation(self, dest=0, height=0,):
        self.background.fill([0,0,0])
        while height < 800:
            if dest <= 800:
                self.spisoc.append(self.background.blit(random.choice(self.kartinka), [dest, height]))
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
        while height < len(map.split('\n'))*self.x:
            for i in map:
                if i!= "\n":
                    image=backgrounds[int(i)]
                # elif i=='2':
                #     image=self.backgrounds[1]*
                # elif i==''
                else:
                    image=None

                if dest <len(map.split('\n'))*self.x and image!=None:
                    if i=='0' or i=='1':
                        self.spisoc.append([self.background.blit(image, [dest, height]),'s',True])

                    else:
                        pass
                        self.spisoc.append([self.background.blit(image, [dest, height]),'g',False])
                    dest+=self.x
                    self.y=self.x
                elif height != len(map.split('\n'))*self.x and i=="\n":
                    height += self.x
                    self.y = self.x
                    dest = 0
                    print(dest)
                elif dest < len(map.split('\n'))*self.x:
                    dest+=self.x




    def restart(self):
        self.x = self.xy
        self.y = self.xy
        self.spisoc.clear()


    def resize_randomizer(self):
        self.pixels = random.randint(4, 40)
        return self.pixels
    def resizer_part(self,map):
        self.pixels = len(map.split('\n'))
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
            self.y = self.kartinka.get_height()*self.x/self.kartinka.get_width()
            self.kartinka=pygame.transform.scale(self.kartinka, [self.x, self.y])
            self.zapreshenaia_kartinka=image_worker.to_grayscale(self.kartinka)
            self.zapreshenaia_kartinka=image_worker.poly_prosrathnost(self.zapreshenaia_kartinka, 150)

