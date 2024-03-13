from pyzbar.pyzbar import *
import cv2
img = cv2.imread("barcode4.png")
Barcode = decode(img)
print("Decode:", Barcode[0].data)
cv2.imshow("img", img)
cv2.waitKey(0)
