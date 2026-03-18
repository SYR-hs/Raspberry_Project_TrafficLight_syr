from gpiozero import LED          # ‘gpiozero’ 라이브러리에서‘LED’  클래스를 가져옴
from time import sleep            # ‘time’ 라이브러리에서‘sleep’ 함수를 가져옴

carLedRed = 2                     # 다양한 LED 핀의 핀번호를 변수로 정의함 (Lines 4 ~ 8)
carLedYellow = 3                  # carLedRed, carLedYellow, carLedGreen, humanLedRed,humanLedGreen 변수에 각각 핀번호를 할당
carLedGreen = 4
humanLedRed = 20
humanLedGreen = 21

carLedRed = LED(2)                 # 각 LED를 LED 클래스의 객체로 초기화하며, 핀번호를 사용하여 LED 객체를 생성(Lines 10 ~ 14)
carLedYellow = LED(3)
carLedGreen = LED(4)
humanLedRed = LED(20)
humanLedGreen = LED(21)

try:                               # 무한루프（while 1:）를 시작, 이 루프에서는 아래의 동작을 반복함(Lines 16 ~ 35)
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
    
except KeyboardInterrupt:          # 사용자가 Ctrl + C를 누를때 까지 코드를 실행하는 예외처리블록임
    pass                           # 사용자가 Ctrl + C를 누르면 루프가 중단되고 코드실행이 종료됨

carLedRed.value = 0                # 코드실행이 종료되면 모든 LED를 꺼줌(Lines 40 ~ 44)
carLedYellow.value = 0
carLedGreen.value = 0
humanLedRed.value = 0
humanLedGreen.value = 0
