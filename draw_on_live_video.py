import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# (Top left corner) divide them by 2 to get integer values
x = width // 2
y = height // 2

# draw a rectangle with size 1/4 of video screen
w = width // 4
h = height // 4

# (Bottom right corner) = x+w, y+h
b = x+w, y+h

while True:
    ret, frame = cap.read()

    # rectangle frame
    cv2.rectangle(frame, (x, y), b,
                  color=(255,0,255),
                  thickness=5)
    # show it
    cv2.imshow('frame', frame)

    if cv2.waitKey(3) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()