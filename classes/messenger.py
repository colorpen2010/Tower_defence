class Messenger():
    def __init__(self):
        self.polythateli=[]
    def podpisatsa(self,polythatel):
        self.polythateli.append(polythatel)
    def otpravit(self,pismo,otpravitel,dop_info=None):
        for i in self.polythateli:
            i(pismo,otpravitel,dop_info)




messenger=Messenger()