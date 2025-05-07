import pygame,math_utils,yaml,os
from classes import animator, enemy_factory, tower_class,plitochniy_zavod,shop,wallet,firetower,poisontower,stormtower,icetower,\
    warehouse,messenger,hp_System,level,portal

class Level:
    def __init__(self,config_map):
        self.font = pygame.font.SysFont('arial', 50)
        self.animated_blue_portal = None
        self.animated_red_portal = None
        self.plitki = []
        self.wallet = wallet.get_wallet(100)
        self.wallet.set_money(100)
        self.mainhp = hp_System.HP_system(50, 50, 500, 500, 100, 30)
        self.route = []
        self._map_generation(config_map)

    def _map_generation(self, map):
        switch = False
        door = []
        etasch = []


        height = 0
        dest = height
        house=[]

        for i in map:
            if i == '[' or switch==True:
                switch=True
                if i==']':
                    switch=False
                    etasch.append(door)
                    door=[]
                elif i!='[':
                    door.append(i)
            if i == ' ':
                if len(etasch)!=0:
                    house.append(etasch)
                    etasch=[]
        razmer_plitki = 800 // (len(house))
        for etasch in house:
            for door in etasch:
                kletka=['sand', dest, height, len(house)]
                for shitel in door:
                    if shitel == '*':
                        kletka[0]='sand'
                    elif shitel == '_':
                        kletka[0]='grass'
                    elif shitel == '(':
                        kletka[0]='sand'
                        kletka.append('(')
                        self.route.append([int(dest + razmer_plitki / 2), int(height + razmer_plitki / 2), 0])
                    elif shitel == ')':
                        kletka[0]='sand'
                        kletka.append(')')
                        self.route.append([int(dest + razmer_plitki / 2), int(height + razmer_plitki / 2), 999])
                    elif shitel.isnumeric():
                        kletka[0]='sand'
                        self.route.append([int(dest + razmer_plitki / 2), int(height + razmer_plitki / 2), int(shitel)])




                self.plitki.append(plitochniy_zavod.Tsekh(kletka[0], kletka[1], kletka[2], kletka[3]))
                if kletka[-1]=='(':
                    # self.animated_blue_portal = animator.Animator('images/Portal/Idle__/blue_idle', 40, len(house), False, x=dest, bottom=height + razmer_plitki)
                    self.animated_blue_portal = portal.Portal('start',len(house),dest,height+razmer_plitki)
                if kletka[-1]==')':
                    # self.animated_red_portal = animator.Animator('images/Portal/Idle__/red_idle', 40, len(house), False, x=dest, bottom=height + razmer_plitki)
                    self.animated_red_portal = portal.Portal('finish',len(house),dest,height+razmer_plitki)
                    self.mainhp.centerx=self.animated_red_portal.get_center()[0]
                    self.mainhp.bottom=self.animated_red_portal.get_rect()[1]
                if dest<pygame.display.get_window_size()[0]-razmer_plitki:
                    dest +=razmer_plitki
                # else:
                # spisoc.append(plitochniy_zavod.Tsekh('grass',dest,height,map))

                else:
                    dest=0
                    height+=razmer_plitki
                self.route.sort(key=lambda element: element[2])
        for o in self.route:
            del o[-1]
        self.house=house
            #     # self.y=self.x

    def paint(self,perecluthatel,enemies):
        screen=pygame.display.get_surface()
        images=[]
        images.append(self.animated_red_portal)
        images.append(self.animated_blue_portal)
        for p in self.plitki:
            p.okraska(screen)
            if p.tower!=None:
                images.append(p.tower)

        images+=enemies
        for i in math_utils.sortirovka(images,self.plitki,level=self):
            i.paint(perecluthatel)
        if perecluthatel:
            shoti = 0
            for u in self.route:
                pygame.draw.circle(screen, [0, 0, 0], u, 10)
                pos = self.font.render(str(shoti), True, [255, 0, 0])
                screen.blit(pos, u)
                shoti += 1




        self.mainhp.paint()


    def controller(self,events):
        if self.animated_blue_portal != None:
            self.animated_blue_portal.control_center(events)
        if self.animated_red_portal != None:
            self.animated_red_portal.control_center(events)

    def give_your_number_of_etashey(self):
        return len(self.house)

    def poisk_kletki(self,pos):
        for i in self.plitki:
            rect = i.get_rect()
            if rect.collidepoint(pos):
                return i
