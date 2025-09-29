import cv2 as cv    
    
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0]* scale)
    
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# # read images
# img = cv.imread('Photos/cat.jpg')


# resized_img = rescaleFrame(img)

# if img is None:
#     print("Error: Could not load image.")
# else:
#     cv.imshow('Cat', img)
    
#     cv.imshow('Cat2', resized_img)

#     # Wait indefinitely until a key is pressed
#     cv.waitKey(0)

#     # Destroy all open OpenCV windows
#     cv.destroyAllWindows()



# read videos
capture = cv.VideoCapture('../Resources/Videos/dog.mp4')

while True:
  isTrue, frame = capture.read()
  
  frame_resized = rescaleFrame(frame, scale= .2)
  
  cv.imshow('Video', frame)
  
  cv.imshow('Video Resized', frame_resized)
  
  if cv.waitKey(20) & 0xFF == ord('d'):
      break

capture.release()
cv.destroyAllWindows()