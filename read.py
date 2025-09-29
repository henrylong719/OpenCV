import cv2 as cv

# # read images
# img = cv.imread('/Resources/Photos/cat.jpg')

# if img is None:
#     print("Error: Could not load image.")
# else:
#     cv.imshow('Cat', img)

#     # Wait indefinitely until a key is pressed
#     cv.waitKey(0)

#     # Destroy all open OpenCV windows
#     cv.destroyAllWindows()


# read videos
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
  isTrue, frame = capture.read()
  
  cv.imshow('Video', frame)
  
  if cv.waitKey(20) & 0xFF == ord('d'):
      break

capture.release()
cv.destroyAllWindows()