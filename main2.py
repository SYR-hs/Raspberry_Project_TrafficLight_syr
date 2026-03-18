from gpiozero import LED     # ‘gpiozero’ 라이브러리에서‘LED’  클래스를가져옴
from time import sleep       # ‘time’ 라이브러리에서‘sleep’ 함수를가져옴

carLedRed = 2                # 다양한LED 핀의핀번호를변수로정의함 (Lines 4 ~ 8)
carLedYellow = 3             # carLedRed, carLedYellow, carLedGreen, humanLedRed,humanLedGreen 변수에각각핀번호를할당
carLedGreen = 4
humanLedRed = 20
humanLedGreen = 21

carLedRed = LED(2)
carLedYellow = LED(3)
carLedGreen = LED(4)
humanLedRed = LED(20)
humanLedGreen = LED(21)

try:
    while 1:
        carLedRed.value = 0
        carLedYellow.value = 0
        carLedGreen.value = 1
        humanLedRed.value = 1
        humanLedGreen.value = 0
        sleep(3.0)
        carLedRed.value = 0
        carLedYellow.value = 1
        carLedGreen.value = 0
        humanLedRed.value = 1
        humanLedGreen.value = 0
        sleep(1.0)
        carLedRed.value = 1
        carLedYellow.value = 0
        carLedGreen.value = 0
        humanLedRed.value = 0
        humanLedGreen.value = 1
        sleep(3.0)
    
except KeyboardInterrupt:
    pass

carLedRed.value = 0
carLedYellow.value = 0
carLedGreen.value = 0
humanLedRed.value = 0
humanLedGreen.value = 0
