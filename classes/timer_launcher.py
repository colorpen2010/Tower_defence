
import pygame.time


class Time():
    def __init__(self):
        self.timer_events=[]
        self.procent=100
        self.center=pygame.event.custom_type()
        pygame.time.set_timer(self.center,10)
        self.time=10
    def create_timer(self,event_number,miliseconds,deef=None):
        # self.shoti(event_number, miliseconds)
        if deef!=None:
            self.timer_events.append([event_number,miliseconds,0,deef])

    def timers_change(self,milisec):
        self.time=milisec
        # self.procent=procent
        # for event in self.timer_events:
        #     self.shoti(event[0],event[1])

    def delete_timer(self,event_number):
    #     pygame.time.set_timer(event_number,0)
        for o in self.timer_events:
            if o[0]==event_number:
                self.timer_events.remove(o)
                print(self.timer_events)


    def shoti(self,event_number,miliseconds):
        pass
        # procent_result = self.procent / 100 * miliseconds
        # pygame.time.set_timer(event_number,0)
        # pygame.time.set_timer(event_number, int(procent_result))


    def controller(self,events):
        for o in events:
            if o.type == self.center:
                self.tec_time=self.time
                while self.everybody_move_your_body()==1:
                    pass


    def everybody_move_your_body(self):
        result = 1
        self.tec_time -= 10
        for i in self.timer_events:
            i[2] += 10
            if i[2] >= i[1]:
                i[3]()
                i[2] -= i[1]
        if self.tec_time<=0:
            result=0
        return result


        # print(self.timer_events)


timer_worker=Time()