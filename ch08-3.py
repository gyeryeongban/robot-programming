# 1. 라이브러리 불러오기
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# one-hot encoding
from tensorflow.keras.utils import to_categorical
# data model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# 2. 데이터 불러오기
# data load
train_csv = pd.read_csv("../input/mnist-in-csv/mnist_train.csv")

# 3. 학습 데이터 준비하기
# obtain the image data
X_train = []
for i in train_csv.index:
    X_train.append(train_csv.iloc[i][1:].values)

# change list to array - data normalization for efficient data learning
x_train = np.array(X_train) / 255.0

# obtain labels
Y_train = train_csv["label"].values
# change to one-hot encoding
y_train = to_categorical(Y_train)

# 4. 모델 만들기
# 1. 입력층의 노드 수: 이미지의 크기 (28x28)
# 2. 은닉층의 개수:
# 3. 각 은닉층의 노드 수: 100
# 4. 출력층의 노드 수: 분류하기 위한 클래스 수 (0 ~ 9)

input_node = 28 * 28
output_node = 10
hidden_node = 100

# deep neural network model
dnn = Sequential()
dnn.add(Dense(hidden_node, activation = "relu", input_shape = (input_node, )))
dnn.add(Dense(output_node, activation = "softmax"))

# loss function & optimizer function
dnn.compile(loss = "categorical_crossentropy", optimizer = "adam", metrics = ["accuracy"])

# run model
dnn_hist = dnn.fit(x_train, y_train, epochs = 15, batch_size = 100, validation_split = 0.2)