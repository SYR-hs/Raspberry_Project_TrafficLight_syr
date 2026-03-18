# 라이브러리 불러오기
from gpiozero import LED            # 라즈베리파이의 GPIO핀을 쉽게 제어할 수 있도록 gpiozero 라이브러리에서 LED 제어 기능을 가져옴
from time import sleep              # 코드 실행을 잠시 멈추도록(대기 시간을 부여함) time 모듈에서 sleep 함수를 가져옴

# 핀 번호 및 LED 설정
                                    # 각 신호등 색상에 해당하는 핀 번호를 변수에 저장함
                                    # (carLed~ : 자동차 신호등 / humanLed~ : 보행자 신호등)
                                    # 아래 코드에서 LED() 라는 객체를 통해 변수를 사용하고 있으므로, 변수 할당 코드는 삭제해도 정상 작동함

carLedRed = 2
carLedYellow = 3
carLedGreen = 4
humanLedRed = 20
humanLedGreen = 21

                                    # LED(핀번호) : gpiozero 에서 사용하는 문법에 따라 각 핀 번호(2, 3, 4, 20, 21)에 연결된 부품이 LED임을 선언 및 제어함
carLedRed = LED(2)
carLedYellow = LED(3)
carLedGreen = LED(4)
humanLedRed = LED(20)
humanLedGreen = LED(21)

# 신호등 동작 루프
try:
    while 1:                        # 아래의 코드 무한 루프
                                    # 자동차 주행 (3초) / value = 1 은 LED 켜기, value = 0 은 LED 끄기
                                    # 자동차 신호등은 초록불 점등, 보행자 신호등은 빨간불 점등, 자동차는 지나가고 보행자는 대기 상태
        carLedRed.value = 0
        carLedYellow.value = 0
        carLedGreen.value = 1
        humanLedRed.value = 1
        humanLedGreen.value = 0
        sleep(3.0)                  # 상태 3초간 유지
        
                                    # 자동차 정지 준비(1초)
                                    # 자동차 신호등은 노란불로 변경, 보행자 신호등은 빨간불로 대기 유지, 신호 변경을 알리는 상태
        carLedRed.value = 0
        carLedYellow.value = 1
        carLedGreen.value = 0
        humanLedRed.value = 1
        humanLedGreen.value = 0
        sleep(1.0)                  # 상태 1초간 유지
        
                                    # 보행자 횡단(3초)
                                    # 자동차 신호등은 빨간불로 변경, 보행자 신호등은 초록불로 변경, 보행자가 횡단함을 알리는 상태
        carLedRed.value = 1
        carLedYellow.value = 0
        carLedGreen.value = 0
        humanLedRed.value = 0
        humanLedGreen.value = 1
        sleep(3.0)                 # 상태 3초간 유지
    
except KeyboardInterrupt:          # 사용자가 터미널에서 Crtl+C 를 눌러 프로그램을 강제 종료하려고 할 때 발생하는 이벤트
    pass                           # 예외가 발생했을 때 프로그램이 에러가 나며 멈추지 않고 다음 코드로 넘어감

                                   # .value = 0 : 프로그램이 완전히 종료되기 직전에 모든 LED의 불을 끄는 것
                                   # 아래의 코드가 없으면 프로그램이 종료되어도 마지막에 켜져 있던 LED의 불이 계속 켜져있게 됨
carLedRed.value = 0
carLedYellow.value = 0
carLedGreen.value = 0
humanLedRed.value = 0
humanLedGreen.value = 0