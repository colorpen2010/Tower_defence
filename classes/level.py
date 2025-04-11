import pygame,math_utils,yaml,os
from classes import animator, enemy_factory, tower_class,plitochniy_zavod,shop,wallet,firetower,poisontower,stormtower,icetower,\
    warehouse,messenger,hp_System,level

class Level:
    def __init__(self):

        self.animated_blue_portal = None
        self.animated_red_portal = None
        self.plitki = []
        self.mainhp = hp_System.HP_system(50, 50, 500, 500, 100, 30)
        self.route = []

    def map_generation(self, map):
        global house,animated_blue_portal,animated_red_portal,mainhp

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
                    animated_blue_portal = animator.Animator('images/Portal/Idle__/blue_idle', 40, len(house), False, x=dest, bottom=height + razmer_plitki)
                if kletka[-1]==')':
                    animated_red_portal = animator.Animator('images/Portal/Idle__/red_idle', 40, len(house), False, x=dest, bottom=height + razmer_plitki)
                    self.mainhp.centerx=animated_red_portal.get_center()[0]
                    self.mainhp.bottom=animated_red_portal.get_rect()[1]
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
            #     # self.y=self.x

    def paint(self,perecluthatel,images):
        screen=pygame.display.get_surface()

        for i in math_utils.sortirovka(images,self.plitki):
            i.paint(perecluthatel)

        for p in self.plitki:
            p.okraska(screen)
        self.mainhp.paint()
        animated_red_portal.paint()
        animated_blue_portal.paint()

    def controller(self,events):
        if self.animated_blue_portal != None:
            self.animated_blue_portal.control_center(events)
        if self.animated_red_portal != None:
            self.animated_red_portal.control_center(events)

    def give_your_towers(self):
        spisok=[]
        for i in self.plitki:
            spisok.append(i)
        return spisok
