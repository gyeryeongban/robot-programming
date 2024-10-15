# Dofbot 모듈 제어

# 라이브러리
import time
from Arm_Lib import Arm_Device

# 로봇팔 객체 생성
Arm = Arm_Device()
time.sleep(.1)

# LED 모듈 제어
def main():
    while True:
        # 빨간불 켜짐
        Arm.Arm_RGB_set(50, 0, 0)
        time.sleep(.5)
        
        # 초록불 켜짐
        Arm.Arm_RGB_set(0, 50, 0)
        time.sleep(.5)
        
        # 파란불 켜짐
        Arm.Arm_RGB_set(0, 0, 50)
        time.sleep(.5)
        
        print("END OF LINE!")
try:
    main()
except KeyboardInterrupt:
    # 로봇팔 객체 해제
    del Arm
    print("Program closed!")
    pass

# Buzzer가 자동으로 0.1초 동안 울린 후 꺼짐
b_time = 1
Arm.Arm_Buzzer_On(b_time)
time.sleep(1)

# Buzzer가 자동으로 0.3초 동안 울린 후 꺼짐
b_time = 3
Arm.Arm_Buzzer_On(b_time)
time.sleep(1)

# Buzzer가 계속 울림
Arm.Arm_Buzzer_On()
time.sleep(1)

# Buzzer가 꺼짐
Arm.Arm_Buzzer_off()
time.sleep(1)

# 로봇팔 객체 해제
del Arm