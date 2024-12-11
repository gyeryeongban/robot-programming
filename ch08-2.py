# MNIST 데이터 전처리
# 라이브러리 Import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from tensorflow.keras.utils import to_categorical

# MNIST 데이터 로드
train_csv = pd.read_csv("../input/mnist-in-csv/mnist_train.csv")

# 2. Tranin set의 모든 데이터를 28x28로 불러오기
# MNIST 데이터 로드
X_train = []
for i in train_csv.index:
    X_train.append(train_csv.iloc[i][1:].values.reshape([28, 28]))

# list를 array로 변환하기
X_train = np.array(X_train)
X_train[0]

# train set의 label
Y_train = train_csv["label"].values

# label이 포함된 시각화
num = 32835
plt.imshow(X_train[num], cmap = "Greys")
print("label: ", Y_train[num])

# 전체 데이터 셋에서 Label 확인하기
np.unique(Y_train)

# Y_train을 one-hot encoding으로 변환하기
y_train = to_categorical(Y_train)

y_train

# One-hot encoding
Y_train

y_train[0]

y_train[1]