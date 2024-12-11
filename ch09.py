import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from tensorflow.keras.utils import to_categorical

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten

train_csv = pd.read_csv("../input/mnist-in-csv/mnist_train.csv")

# 데이터 전처리
X_train = []
for i in train_csv.index:
    X_train.append(train_csv.iloc[i][1:].values.reshape([28, 28]))

x_train = np.array(X_train) / 255.0

W = 28
H = 28
x_train = x_train.reshape(len(train_csv), W, H, 1)

Y_train = train_csv["label"].values
y_train = to_categorical(Y_train)

# 데이터 구조
# - dnn 모델의 데이터 구조
#     - x_train: (60000, 784) # 28 * 28
#     - y_train: (60000, 10)
#     - x_test: (10000, 784)
#     - y_test: (10000, 10)

print("x_train: ", x_train.shape)
print("y_train: ", y_train.shape)

# CNN 모델 만들기
cnn = Sequential()
# Convolution Layer
cnn.add(Conv2D(filter = 32, kernel_size = (3, 3). activation = "relu", input_shape = (W, H, 1)))
cnn.add(MaxPooling2D(pool_size = (2, 2))) # Pooling Layer
cnn.add(Flatten()) # Change input data to 1 dimension

cnn.add(Dense(128, activation = "relu")) # Fully Connected Layer
cnn.add(Dense(10, activation = "softmax")) # Softmax

cnn.compile(loss = "categorical_crossentropy", optimizer = "adam", metrics = ["accuracy"])

# 모델 학습하기
cnn_hist = cnn.fit(x_train, y_train, epochs = 15, batch_size = 100, validation_split = 0.2)

# 모델 시각화
plt.plot(cnn_hist.history["accuracy"], label = "acc")
plt.plot(cnn_hist.history["val_accuracy"], label = "val_acc")
plt.legend()
plt.zlabel("epoch")
plt.ylabel("accuracy")

# 모델 평가하기
pred = cnn.predict(x_test)

pred[10]

pred_num = []
for k in pred:
    pred_num.append(k.argmax())

count = 0
pred_err = []
for k in range(len(x_test)):
    if pred_num[k] == Y_test[k]:
        count = count + 1
    else:
        pred_err.append(k)
    
print(count)

print("cnn 모델 정확도: ", count / len(x_test) * 100, "%")

img = test_csv.iloc[pred_err[15]][1:].values.reshape([28, 28])
plt.imshow(img, cmap = "Greys")
print("Label: ", Y_test[pred_err[15]])
print("Prediction: ", pred_num[pred_err[15]])