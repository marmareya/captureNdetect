import cv2

# our stored video
cap = cv2.VideoCapture('myvideo.mkv')

# if the video path was wrong, print this
if cap.isOpened() == False:
    print('Error! Check your file path.')

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        # show it
        cv2.imshow('frame', frame)

        if cv2.waitKey(15) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()