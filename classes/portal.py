from classes import animator

class Portal(animator.Animator):
    def __init__(self,type,visota,x,bottom):
        self.type=type
        if type=='start':
            pyt='images/Portal/Idle__/blue_idle'
        elif type=='finish':
            pyt='images/Portal/Idle__/red_idle'
        else:
            raise Exception('type must be start or finish')

        animator.Animator.__init__(self,pyt,40,visota,x=x,bottom=bottom)
