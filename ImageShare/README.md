These are the instructions to set up Multiuser-Image-Privacy-Tool on your computer.

REQUIRED:
Download YOLOv3 weights (248 MB) and place file in python/yolo_coco:
	command line:
		wget https://pjreddie.com/media/files/yolov3.weights
	

Set the directory files will upload to when user clicks 'upload':
	1. go to src/main/resources/application.properties page
	2. change 'file.upload-dir' to desired directory

Set the python interpreter path (FileController.java):
	Line 31: set 'pythonPath' to python interpreter path on your local machine
	
	
Optional:
YOLOv3 Object Detection set up (object_detection.py):
	The project creates the directory "YOLOoutput" within this project to store YOLOv3 outputs.
	Line 17: change to store in another directory.

Facial Detection set up (facial_detection.py):
	This project creates directories "FacesExtracted" and "groupPhoto" within the project directory to store image outputs.
	Line 56 & 58: change to create new directories to store outputs.