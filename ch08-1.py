# MNIST 데이터 로드 및 시각화
# 1. Import Library
    # - numpy: 행렬이나 다차원 배열 처리
    # - pandas: 테이블 방식 데이터 처리
    # - matplotlib: 데이터 시각화

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 2. Load Data Set
    # 1. add data
    # 2. search data set: mnist in csv(comma seperated values)
    # 3. add
    # 4. input

# read csv
train_csv = pd.read_csv("../input/mnist-in-csv/mnist_test.csv")

train_csv

train_csv.iloc[0]

train_csv.iloc[0].values

# 첫 번째 행의 값을 28x28 배열로 변경하기
img_1 = train_csv.iloc[0][1:].values.reshape([28, 28])
img_1

# 데이터 시각화
plt.imshow(img_1, cmap = "Greys")

# 다른 행의 데이터 시각화
row = 15
img = train_csv.iloc[row][1:].values.reshape([28, 28])
plt.imshow(img, cmap = "Greys")