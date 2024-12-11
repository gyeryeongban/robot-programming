import cv2
import sys
import matplotlib,pyplot as plt

# image loading
img = cv2.imread('/kaggle/input/images/rabbit.jpg', 1) # read an image
print(img.shape) # image shape
plt.imshow(img)
plt.show()

# image resizing
x, y = img.shape[0:2]
img_test1 = cv2.resize(img, (int(y / 2), int(x / 2)))
img_test2 = cv2.resize(img, (0, 0), fx = 0.25, fy = 0.25, interpolation = cv2.INTER_NEAREST)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # change BRG to RGB; opencv loads an image as BGR
dst1 = cv2.cvtColor(img_test1, cv2.COLOR_BGR2RGB)
dst2 = cv2.cvtColor(img_test2, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.show()
plt.imshow(dst1)
plt.show()
plt.imshow(dst2)
plt.show()

# image rotation
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
rotate = cv2.getRotationMatrix2D((height * 0.5, width * 0.5), 45, 1) # center, angle, scale
dst = cv2.warpAffine(img, rotate, (height, width))

plt.imshow(dst)
plt.show()

# Binary Image
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh1 = cv2.threshold(grayImg, 10, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(grayImg, 10, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(grayImg, 10, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(grayImg, 10, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(grayImg, 10, 255, cv2.THRESH_TOZERO_INV)

titles = ['Gray Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [grayImg, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

# edge detection
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgG = cv2.GaussianBlur(gray, (3, 3), 0) # Blurring (smoothing)
dst = cv2.Canny(img, 50, 50) # edge ditection

img_bgr2rgb1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_bgr2rgb1)
plt.show()

img_bgr2rgb2 = cv2.cvtColor(imgG, cv2.COLOR_BGR2RGB)
plt.imshow(img_bgr2rgb2)
plt.show()

img_bgr2rgb3 = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
plt.imshow(img_bgr2rgb3)
plt.show()