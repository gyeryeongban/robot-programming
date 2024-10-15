# Dofbot 블록 옮기기

# 라이브러리
import time
from Arm_Lib import Arm_Device

# 로봇팔 객체 생성
Arm = Arm_Device()
time.sleep(.1)

# 물체를 집는 동작
# 블록을 잡는 기능 정의
    # enable = 1 : 잡기
    # enable = 0 : 놓기
def arm_clamp_block(enable):
    if enable == 0:
        Arm.Arm_serial_servo_write(6, 60, 400)
    else:
        Arm.Arm_serial_servo_write(6, 130, 400)
        time.sleep(.5)

# 로봇팔의 움직임 제어 -> p = [각 서브 모터의 각도 리스트]
# 이동 로봇 팔의 기능을 정의 및 1번부터 5번까지의 서보 모터를 동시에 제어
    # p = [s1, s2, s3, s4, s5]
def arm_move(p, s_time = 500):
    for i in range(5):
        id = i + 1
        if id == 5:
            time.sleep(.1)
            Arm.Arm_serial_servo_write(id, p[i], int(s_time * 1.2))
        elif id == 1:
            Arm.Arm_serial_servo_write(id, p[i], int(3 * s_time / 4))
        else:
            Arm.Arm_serial_servo_write(id, p[i], int(s_time))
        time.sleep(.01)
    time.sleep(s_time / 1000)

# 로봇팔의 움직임 제어
# 로봇팔이 위로 움직임
def arm_move_up():
    Arm.Arm_serial_servo_write(2, 90, 1500)
    Arm.Arm_serial_servo_write(3, 90, 1500)
    Arm.Arm_serial_servo_write(4, 90, 1500)
    time.sleep(.1)

# 블록의 초기 위치 및 좌표 설정
# 다른 위치에서 변수 매개변수를 정의
p_mould = [90, 130, 0, 0, 90]
p_top = [90, 130, 0, 0, 90]
p_Brown = [90, 53, 33, 36, 270]
p_Yellow = [65, 22, 64, 56, 270]

# 블록 집기 준비
arm_clamp_block(0)
arm_move(p_mould, 1000)
time.sleep(1)

# 노란색 블록 집기
arm_move(p_top, 1000)
arm_move(p_Yellow, 1000)
arm_clamp_block(1)
arm_move(p_top, 1000)
arm_move(p_layer_1, 1000)
arm_clamp_block(0)
time.sleep(.1)
arm_move(p_mould, 1100)

# 동작 종료
# 로봇팔 객체 해제
del Arm