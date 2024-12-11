# 라이브러리 불러오기
# 수치 계산을 할 때
import numpy as np
# 동작에서 지연 시간을 주고 싶을 때
import time
# 모델을 불러올 때
import onnxruntime as rt
# 사진을 찍고, 이미지를 불러올 때
from PIL import Image
import cv2
# dofbot을 제어하고 싶을 때
from Arm_Lib import Arm_Device

# 제어 준비
Arm = Arm_Device()

# 머리를 상하로 움직이는 동작
    # - 위치에 따라 다양하게 값 변경
# 머리를 상하로 움직이도록 하는 함수
def head_shake(angle, s_time):
    for i in range(3):
        Arm.Arm_serial_servo_write6(90, 110, 1, angle, 90, 100, s_time)
        time.sleep(s_time / 1000)
        Arm.Arm_serial_servo_write6(90, 110, 1, angle, 90, 100, s_time)
        time.sleep(s_time / 1000)
        i += 1
    Arm.Arm_serial_servo_write6(90, 110, 1, angle, 90, 100, s_time)

# 각 모듈의 각도를 변경하여 동작 제어
def ctrl_all_servo(angle, s_time):
    Arm.Arm_serial_servo_write6(angle, 180 - angle, angle, angle, angle, angle, s_time)
    time.sleep(s_time / 1000)

# 앞으로 이동 -> 종이컵 집기 -> 들어올리기 -> 옮기기 -> 내리기 -> 놓기 -> ...
Arm.Arm_serial_servo_write6(90, 20, 80, 80, 90, 10, 1000) # go
time.sleep(1)
Arm.Arm_serial_servo_write6(90, 20, 80, 80, 90, 110, 1000) # pick
time.sleep(1)
Arm.Arm_serial_servo_write6(90, 120, 1, 80, 90, 110, 1000) # up
time.sleep(1)