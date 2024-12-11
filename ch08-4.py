# library 불러오기
import numpy as np # 배열 기반 수치 계산
import pandas as pd # 데이터 로딩
import matplotlib.pyplot as plt # 데이터 시각화

from tensorflow.keras.utils import to_categorical # one-hot encoding
from tensorflow.keras.models import Sequential # 모델 만들기
from tensorflow.keras.layers import Dense # 모델 만들기

# 데이터 불러오기
train_csv = pd.read_csv("../input/mnist-in-csv/mnist_train.csv")
test_csv = pd.read_csv("../input/mnist-in-csv/mnist_test.csv")

X_train = []
for i in train_csv.index:
    X_train.append(train_csv.iloc[i][1:].values)

x_train = np.array(X_train) / 255.0

X_test = []
for j in test_csv.index:
    X_test.append(test_csv.iloc[j][1:].value)

x_test = np.array(X_test) / 255.0

Y_train = train_csv["label"].values
Y_test = test_csv["label"].values

y_train = to_categorical(Y_train)
y_test = to_categorical(Y_test)

print("x_train: ", x_train.shape)
print("y_train: ", y_train.shape)
print("x_test: ", x_test.shape)
print("y_test: ", y_test.shape)

input_node = 28 * 28
output_node = 10
hidden_node = 100

dnn = Sequential()
dnn.add(Dense(hidden_node, activation = "relu", input_shape = (input_node, )))
dnn.add(Dense(output_node, activation = "softmax"))

dnn.compile(loss = "categorical_crossentropy", optimizer = "adam", metrics = ['accuracy'])

dnn_hist = dnn.fit(x_train, y_train, epochs = 15, batch_size = 100, validation_split = 0.2)

# 모델 평가하기
pred = dnn.predict(x_test)
pred

pred[0]

Y_test[0]

pred[0].argmax()

pred_num = []
for i in pred:
    pred_num.append(i.argmax())

pred_num[:10]

Y_test[:10]

count = 0
for i in range(10000): # for # of images
    if pred_num[i] == Y_test[i]:
        count = count + 1

count

print("Accuracy: ", count / 10000 * 100, "%")