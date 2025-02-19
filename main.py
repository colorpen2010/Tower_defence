import time
import paint,controller

# def defed(d):
#     return d[1]
#
# spisok=[[1,5,9],[2,4,10],[3,3,8]]
# print(spisok)
# spisok.sort(key=defed)
# print(spisok)
# exit()

while True:
    time.sleep(0.01)
    controller.control()
    paint.risovanie()


