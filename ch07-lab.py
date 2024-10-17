import time
from Arm_Lib import Arm_Device
Arm = Arm_Device()
time.sleep(.1)

# 블록 집기
def arm_clamp_block(enable):
    # 블록 놓기
    if enable == 0:
        Arm.Arm_serial_servo_write(6, 60, 400)
    # 블록 잡기
    else:
        Arm.Arm_serial_servo_write(6, 130, 400)
        time.sleep(.5)

# 로봇팔의 움직임 제어
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
        time.sleep(.1)
    time.sleep(s_time/1000)

# 로봇팔의 움직임 제어 수정
# def arm_move_modify(p, s_time = 500):
#     for i in range(4):
#         id = i + 1
#         if id == 5:
#             time.sleep(.1)
#             Arm.Arm_serial_servo_write(id, p[i], int(s_time * 1.2))
#         elif id == 1:
#              Arm.Arm_serial_servo_write(id, p[i], int(3 * s_time / 4))
#         else:
#              Arm.Arm_serial_servo_write(id, p[i], int(s_time))
#         time.sleep(.1)
#     time.sleep(s_time / 1000)

# 로봇팔 위로 움직이기
def arm_move_up():
    Arm.Arm_serial_servo_write(2, 90, 1500)
    Arm.Arm_serial_servo_write(3, 90, 1500)
    Arm.Arm_serial_servo_write(4, 90, 1500)
    time.sleep(.1)

# 블록의 초기 위치 및 좌표 설정
p_mould = [90, 130, 0, 0, 90]
p_top = [90, 80, 50, 50, 270]
p_Yellow = [65, 22, 64, 56, 270]
p_Red = [115, 22, 64, 56, 270]
p_Green = []
p_Blue = []
# p_layer_4 = [90, 117, 33, 36, 270]
# p_layer_3 = [90, 99, 33, 36, 270]
# p_layer_2 = [90, 71, 33, 36, 270]
# p_layer_1 = [90, 53, 33, 36, 270]
p_layer_4 = [90, 102, 35, 30, 270]
p_layer_3 = [90, 84, 35, 30, 270]
p_layer_2 = [90, 66, 35, 30, 270]
p_layer_1 = [90, 48, 35, 30, 270]

# 블록 집기 준비
arm_clamp_block(0) # 블록 놓기
arm_move(p_mould, 1000)
time.sleep(1)

# arm_clamp_block(0) # 블록 놓기
# arm_move_up()

# 1층 블록 쌓기
arm_move(p_top, 1000)
arm_move(p_Yellow, 1000)
arm_clamp_block(1) # 블록 잡기
arm_move(p_top, 1000)
arm_move(p_layer_1, 1000)
arm_clamp_block(0) # 블록 놓기

# arm_move(p_mould, 1100)
# time.sleep(.1)
# arm_move2(p_layer_1, 1000)
# arm_clamp_block(1) # 블록 잡기

# 2층 블록 쌓기
arm_move(p_top, 1000)
arm_move(p_Red, 1000)
arm_clamp_block(1) # 블록 잡기
arm_move(p_top, 1000)
arm_move(p_layer_2, 1000)
arm_clamp_block(0) # 블록 놓기

# 3층 블록 쌓기
arm_move(p_top, 1000)
arm_move(p_Green, 1000)
arm_clamp_block(1) # 블록 잡기
arm_move(p_top, 1000)
arm_move(p_layer_3, 1000)
arm_clamp_block(0) # 블록 놓기

# 4층 블록 쌓기
arm_move(p_top, 1000)
arm_move(p_Blue, 1000)
arm_clamp_block(1) # 블록 잡기
arm_move(p_top, 1000)
arm_move(p_layer_4, 1000)
arm_clamp_block(0) # 블록 놓기

# arm_move(p_Red_top, 1000)
# arm_move(p_mould, 1000)

del Arm