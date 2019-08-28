# import the necessary packages
import argparse
import cv2
import os

if __name__=="__main__":
     # local python directory path
    python_dir = os.path.dirname(os.path.abspath(__file__))
    
    # local project directory path
    project_dir = os.path.dirname(python_dir)
    
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
                    help="path to input image")
    
    args = vars(ap.parse_args())
    
    # Reading the image as it is
    image = cv2.imread(args["image"],1)
    
    # dimension array
    dimensions = image.shape
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    
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
    
    try:
        os.makedirs("FacesExtracted")
    except FileExistsError:
        pass
    
    try:
        os.makedirs("groupPhoto")
    except FileExistsError:
        pass
    
    # Store predicted faces in this directory
    store_faces_path = os.path.join(project_dir, 'FacesExtracted')
    # Store the group photo in this directory
    store_image_path = os.path.join(project_dir, 'groupPhoto')
    
    image_directory = os.listdir(store_image_path)
    
    image_num = len(image_directory) + 1
    face_counter = 0
    for (x, y, w, h) in faces:
        face_name = "image" + str(image_num) + "face_" + str(face_counter) + ".jpg"
        roi_color = image[y:y + h, x:x + w]
        cv2.imwrite(os.path.join(store_faces_path, face_name), roi_color)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0,255,0), 14)
        face_counter += 1
        print("[INFO] Object found. Saving locally.")
    
    
    # resizes the output to 900x900 image
    resize_image = cv2.resize(image, (900, 900))
    
    
    image_name = "image" + str(image_num) + ".jpg"
    result = cv2.imwrite(os.path.join(store_image_path, image_name), resize_image)
    
    print("[INFO] Image faces_detected.jpg written to filesystem: ", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
