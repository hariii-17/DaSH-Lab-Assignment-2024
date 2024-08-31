#Face Detection from Image
import cv2
image_path="input_image.jpg" #Any image file
img=cv2.imread(image_path)
print(img.shape)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #grayscale image
print(gray_image.shape)
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") #For detecting frontal face
face = face_classifier.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)) #scale factor scales down size of image, minNeighbours provides sliding windows as rect to detect face, minsize is the minimum size of the object that has to be detected
for (x, y, w, h) in face:cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
import matplotlib.pyplot as plt
plt.figure(figsize=(20,10))
plt.imshow(img_rgb)
plt.axis('off')

#Face Detection from Realtime vdo
video_capture = cv2.VideoCapture(0) #Captures vdo from the default camera in the device function to detect faces
def detect_face(vid):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return faces

while True:

    result, video_frame = video_capture.read()  # read frames from the video
    if result is False:
        break  # terminate the loop if the frame is not read successfully
    face = detect_face(video_frame)
    cv2.imshow("Face Detection Project", video_frame)  # displays the processed frame in a window named "Face Detection Project"
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()


