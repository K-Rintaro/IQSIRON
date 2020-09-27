import sys
import pyocr
import cv2
import numpy as np
from PIL import Image
image = "test.jpg" #defined the picture here so you can change path as you like.
name = "test"

#original image
moto = cv2.imread(image)
cv2.imwrite("first.jpg",moto)

#gamma correction
def gammasuruyo(gamma, img):
  gamma_cvt = np.zeros((256,1), dtype=np.uint8)
  for i in range(256):
    gamma_cvt[i][0] = 255*(float(i)/255)**(1.0/gamma)
  return cv2.LUT(img, gamma_cvt)
gamma = gammasuruyo(2, moto)
moto = cv2.hconcat([moto, gamma])
cv2.imwrite("second.jpg",moto)


#gray scale
moto = cv2.cvtColor(moto, cv2.COLOR_BGR2GRAY)
cv2.imwrite("third.jpg",moto)

#thresholding
moto = cv2.threshold(
    moto
    , 200
    , 255
    , cv2.THRESH_BINARY
)[1]

#monochrome inversion
moto = cv2.bitwise_not(moto)
cv2.imwrite("base.jpg", moto)

#character detection
kensyutu = pyocr.get_available_tools()
if len(kensyutu) == 0:
    print("ERROR!!")
    sys.exit(1)
zero = kensyutu[0]
text = zero.image_to_string(
    Image.open("base.jpg"),
    lang="jpn",
    builder=pyocr.builders.TextBuilder()
    )

print(text)