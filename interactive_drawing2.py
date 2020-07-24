import cv2

def draw_circle(event, x, y, flags, param):

    global center, clicked
    # get the mouse click up/down track the center
    if event == cv2.EVENT_LBUTTONDOWN:
        center=(x,y)
        clicked = False

    if event == cv2.EVENT_LBUTTONUP:
        clicked = True

# initial values
center = (0,0)
clicked = False

# capture a video
cap = cv2.VideoCapture(0)

# create a named window for the connections
cv2.namedWindow('Testing')

# bind our function with the mouse clicks
cv2.setMouseCallback('Testing', draw_circle)

while True:
    # capture the frame
    ret, frame = cap.read()

    #check if clicking is True
    if clicked:
        # draw a circle frame
        cv2.circle(frame,
                   center=center,
                   radius=50,
                   color=(255,0,255),
                   thickness=3)

    # display the frame
    cv2.imshow('Testing', frame)

    if cv2.waitKey(3) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
