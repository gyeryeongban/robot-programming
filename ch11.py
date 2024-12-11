# 이미지 캡처와 JPEG 바이너리 변환
    # - 현재 Jupyter notebook 버전 차이로 인한 디스플레이 위젯 생성 불가능
    # - 이미지에 대한 정보 출력 시 -> 정상 실행
# 필요한 라이브러리들을 임포트
import cv2
import ipywidgets.widgets ad widgets
from IPython.display import display

# 이미지 디스플레이 위젯 생성
image_widget = widgets.Image(format = 'jpeg', width = '600', height = 500)
display(image_widget)

# BGR 이미지 데이터를 JPEG 형식으로 변환하는 함수
def bgr8_to_jpeg(value, quality = 75):
    # OpenCV의 imencode 함수는 이미지를 특정 포맷으로 인코딩
    # '.jpg' 포맷으로 이미지를 변환하고, 첫 번째 반환값을 사용, 이미지 데이터를 바이트 형태로 반환

    return bytes(cv2.imencode('.jpg', value)[1])
# 웹캠 초기화
image = cv2.VidepCapture(0, cv2.CAP_V4L2)
# 프레임 캡처 및 위젯 업데이트
ret, frame = image.read()
image_widget.value = bgr8_to_jpeg(frame)

# 라이브러리 import 및 함수 정의
# 필요한 라이브러리들을 임포트
import cv2
import time
import numpy as np

# BGR 이미지 데이터를 JPEG 형식으로 변환하는 함수
def bgr8_to_jpeg(value, quality = 75):
    # OpenCV의 imencode 함수는 이미지를 특정 포맷으로 인코딩
    # '.jpg' 포맷으로 이미지를 변환하고, 첫 번째 반환값을 사용, 이미지 데이터를 바이트 형태로 반환
    return bytes(cv2.imencode('.jpg', value)[1])

# HSV 값 판별 함수 선언
# 이미지를 받아 특정 영역의 색상을 분석하고, 그 색상이 어떤 색인지를 판별
def get_color(img):
    H = []
    color_name = {}
    # 이미지를 640x480 크기로 리사이즈
    img = cv2.resize(img, (640, 480), )

    # 이미지를 BGR에서 HSV 색상 공간으로 변환
    HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 직사각형 영역 내의 모든 픽셀에서 H (색상) 값만 추출하여 H 리스트에 저장
    cv2.rectangle(img, (280, 180), (360, 260), (0, 255, 0), 2)
    for i in range(280, 360):
        for j in range(180, 260): H.append(HSV[j, i][0])
    
    # H 리스트에서 최소값(H_min)과 최대값(H_max)을 구함
    H_min = min(H); H_max = max(H)
    print(H_min, H_max)

    if H_min >= 0 and H_max <= 10 or H_min >= 156 and H_max <= 180:
        color_name['name'] = 'red'
    elif H_min >= 26 and H_max <= 34:
        color_name['name'] = 'yellow'
    elif H_min >= 35 and H_max <= 78:
        color_name['name'] = 'green'
    elif H_min >= 100 and H_max <= 124:
        color_name['name'] = 'blue'
    
    # 색상 이름을 출력
    print(color_name)
    return img, color_name

# 블록 색 인식 -> 코드 실행 후, 카메라로 결과 확인
# 웹캠에서 비디오 캡처를 시작하고, 비디오의 크기 및 프레임 속도를 설정
# 기본 웹캠을 사용하여 비디오 캡처
cap = cv2.VideoCapture(0)
# 가로 크기 설정
cap.set(3, 640)

# 세로 크기 설정
cap.set(4, 480)

# 프레임 속도 설정
cap.set(5, 30)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('M', 'J', 'P', 'G'))

# 기본 색상 범위 (HSV 색상 공간에서 빨간색 범위 설정)
color_lower = np.array([0, 43, 46])
color_upper = np.array([10, 255, 255])

# 색상 인식을 위한 함수
def Color_Recongnize():
    while(1):
        # 웹캠에서 프레임을 읽음
        ret, frame = cap.read()
        if not ret:
            print("웹캠에서 프레임을 읽을 수 없습니다.")
            break

frame, color_name = get_color(frame)

# 색상 변경: 인식된 색상에 따라 범위 설정
if len(color_name) == 1:
    global color_lower
    global color_upper

    if color_name['name'] == 'yellow':
        color_lower = np.array([26, 43, 46])
        color_upper = np.array([34, 255, 255])
    
    elif color_name['name'] == 'red':
        color_lower = np.array([0, 43, 46])
        color_upper = np.array([10, 255, 255])
    
    elif color_name['name'] == 'green':
        color_lower = np.array([35, 43, 46])
        color_upper = np.array([77, 255, 255])
    
    elif color_name['name'] == 'blue':
        color_lower = np.array([100, 43, 46])
        color_upper = np.array([124, 255, 255])
    
    # 원본 영상 출력
    cv2.imshow('Capture', frame)

    # HSV로 변환
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 색상 범위에 맞는 마스크 생성
    mask = cv2.inRange(hsv, color_lower, color_upper)
    cv2.imshow('Mask', mask)

    # 마스크를 적용한 결과 이미지
    res = cv2.bitwise_and(frame, frame, mask = mask)
    cv2.imshow('Result', res)

    # 10ms 대기
    time.sleep(0.01)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 비디오 캡처 해저 및 창 닫기
cap.release()
cv2.destroyAllWindows() # 모든 OpenCV 창 닫기

# 함수 실행
Color_Recongnize()