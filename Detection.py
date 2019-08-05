
# import the necessary packages

import cv2
import os # path

# Reading the image as it is
image = cv2.imread ("/Users/ravipatel/Desktop/val2017/2017_30622680.jpg",1)

# dimension array
dimensions = image.shape
height = image.shape[0]
width = image.shape[1]
channels = image.shape[2]


print('Image Dimension    : ',dimensions)
print('Image Height       : ',height)
print('Image Width        : ',width)
print('Number of Channels : ',channels)

if (width < 1100):
    scaleFactor =1.3

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.5,
    minNeighbors= 3,
    minSize=(50, 50)
)

print("[INFO] Found {0} Faces.".format(len(faces)))

#path for images extracted that needs to be stored
path = '/Users/ravipatel/Desktop/Extract'

for (x, y, w, h) in faces:
    roi_color = image[y:y + h, x:x + w]
    cv2.imwrite(os.path.join(path, str(x) + str(y) + "_faces.jpg"), roi_color)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0,255,0), 14)

    print("[INFO] Object found. Saving locally.")

#group photo showing detection
extract = '/Users/ravipatel/Desktop/Group'

status = cv2.imwrite(os.path.join(extract,'faces_detected.jpg'), image)

print("[INFO] Image faces_detected.jpg written to filesystem: ", status)
cv2.imshow("Output",image)


cv2.waitKey(10000)

