import pygame, random, image_worker


class generation():
    def __init__(self, backgrounds, backgrounds2=None, background=None, types=0, xy=50):
        self.xy = xy
        self.x = xy
        self.y = xy
        self.kartinka = backgrounds
        self.type = types
        self.zapreshenaia_kartinka = backgrounds2
        self.background = background
        self.backgrounds = backgrounds
        self.spisoc = []
        self.pixels = 10
        self.grass_or_sand = []

    def map_regeneration(self, map, korobka_s_plitami):
        height = 0
        kolvo_strok = len(map.split('\n'))
        visota_pola = kolvo_strok * self.x

        dest = height
        for i in map:
            if i != "\n":
                image = korobka_s_plitami[int(i)]
            else:
                image = None

            if dest < visota_pola and image != None:
                rectik = self.background.blit(image, [dest, height])
                if i == '0' or i == '1':
                    self.spisoc.append({'rect':rectik, 'type':'s', 'building':False})


                else:
                    self.spisoc.append({'rect':rectik, 'type':'g', 'building':False})
                dest += self.x
                # self.y=self.x
            elif height != visota_pola and i == "\n":
                height += self.x
                # self.y = self.x
                dest = 0

    def resize_randomizer(self):
        self.pixels = random.randint(4, 40)
        return self.pixels

    def resizer_part(self, map):
        self.pixels = len(map.split('\n'))
        return self.pixels

    def resive(self, pixels=10):
        kva=[]
        self.pixels = pixels
        if self.type == 0:
            for o in self.backgrounds:
                self.x = round(800 / self.pixels, 0)
                self.y = self.x
                self.xy = self.x
                kva.append(pygame.transform.scale(o, [self.x, self.y]))
            self.backgrounds.clear()
            for i in kva:
                self.backgrounds.append(i)
        if self.type == 1:
            self.x = round(800 / self.pixels, 0)
            self.y = self.kartinka.get_height() * self.x / self.kartinka.get_width()
            self.kartinka = pygame.transform.scale(self.kartinka, [self.x, self.y])
            self.zapreshenaia_kartinka = image_worker.to_grayscale(self.kartinka)
            self.zapreshenaia_kartinka = image_worker.poly_prosrathnost(self.zapreshenaia_kartinka, 150)

