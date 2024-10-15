# 로봇팔 각도 제어

# 라이브러리
# 수치 계산할 때
import numpy as np
# 동작에서 지연 시간을 주고 싶을 때
import time
# 모델을 불러올 때
import onnxruntime as rt
# 사진을 찍고 이미지를 불러올 때
from PIL import Image
import cv2
# Dofbot을 제어하고 싶을 때
from Arm_Lib import Arm_Device

# 제어 준비
Arm = Arm_Device()

# Arm.Arm_serial_servo_write6(1번, 2번, 3번, 4번, 5번, 6번, 동작 시간)
    # 1, 5번 모듈: 좌우 움직임(-180 ~ 180)
    # 2, 3, 4번 모듈: 상하 움직임(2번: 80 ~ 180, 3번: 1 고정)
    # 6번 모듈: 집게가 벌어지는 정도
    # 동작 시간: 숫자가 클수록 천천히 동작함
def ctrl_all_servo(angle, s_time):
    Arm.Arm_serial_servo_write6(angle, 180-angle, angle, angle, angle, angle, s_time)
    time.sleep(s_time / 1000)

def armdance():
    for i in range(2):
        for angle in [20, 90, 160, 90]:
            ctrl_all_servo(angle, 1000)
            time.sleep(10 / 1000)
        i += 1
    Arm.Arm_serial_servo_write6(90, 110, 1, 40, 90, 100, 1000)

armdance()
print("zerobot dance dance~")