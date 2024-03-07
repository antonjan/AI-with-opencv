
"""
Created on Thu Dec 28 12:55:48 2023
@author: mh.olyaei@yahoo.com
"""
from pyzbar.pyzbar import *
import cv2
img = cv2.imread("barcode(3).png")
Barcode = decode(img)
print("Decode:", Barcode[0].data)
cv2.imshow("img", img)
cv2.waitKey(0)
