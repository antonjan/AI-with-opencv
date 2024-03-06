import cv2
model = cv2.CascadeClassifier('face_detector.xml')
img = cv2.imread('image.jpg')
faces = model.detectMultiScale(img, 1.1, 4)
for (x, y, w, h) in faces: 
  cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
cv2.imwrite("face_detected.png", img) 
print('output saved')
