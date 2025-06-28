### Basic operations with OpenCV
# using Python
import cv2

# Operation-1: Read the image from directory
# image = cv2.imread("image.jpg")
image = cv2.imread(r"D:\Kainovation Projects\PPE_2025_06_25\Exercise Files\01-02\image.jpg")

# ..................................
# Operation-2: Blur the image
blurred = cv2.blur(image, (50, 50))
#..................................

# print("Image shape:", image.shape)  # Print the shape of the image

# Operation-3: Visualize the image
# cv2.imshow("test", blurred)
# cv2.waitKey(0)  # display until key press
#........................

# Operation-4: Write the image in directory
# cv2.imwrite("Exercise Files/01-02/test.png", blurred)
# ...................

# Operation-5: Crop the image and display it
# sliced_image = image[240:450, 680:900]
# cv2.imshow("sliced_window", sliced_image)
# cv2.waitKey(0)
# .................................


# Operation-6: Read and process video file
# videocapture = cv2.VideoCapture("video.mov")
videocapture = cv2.VideoCapture("D:\\Kainovation Projects\\PPE_2025_06_25\\Exercise Files\\01-02\\video.mov")

while videocapture.isOpened():
    success, frame = videocapture.read()
    if success:
        cv2.imshow("test", frame)
        if cv2.waitKey(2) & 0xFF == ord("q"):
            break
    else:
        break  # break the window once frames completed
# .......................
