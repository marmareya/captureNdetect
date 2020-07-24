import cv2

# callback function for the mouse/rectangle
def draw_rectangle(event, x, y, flags, param):
    global pt1, pt2, top_left_clicked, bottom_right_clicked

    # Create event for left button down
    if event == cv2.EVENT_LBUTTONDOWN:
        if top_left_clicked == True and bottom_right_clicked == True:
            pt1 = (0, 0)
            pt2 = (0, 0)
            top_left_clicked = False
            bottom_right_clicked = False

        if top_left_clicked == False:
            pt1 = (x, y)
            top_left_clicked = True

    elif bottom_right_clicked == False:
        pt2 = (x, y)
        bottom_right_clicked = True

# set global values for pt1 & pt2
pt1 = (0, 0)
pt2 = (0, 0)

# Trackers are false
top_left_clicked = False
bottom_right_clicked = False

# capture a video
cap = cv2.VideoCapture(0)

# create a named window for the connections
cv2.namedWindow('Test')

# set a mouse callback
cv2.setMouseCallback('Test', draw_rectangle)

while True:
    # capture the frame
    ret, frame = cap.read()

    # Draw the frame based on the global variables
    if top_left_clicked == True:
        cv2.circle(frame,
                   center=pt1,
                   radius=5,
                   color=(255, 0, 255),
                   thickness=-1)

    # Draw a rectangle on the frame
    if top_left_clicked == True and bottom_right_clicked == True:
        cv2.rectangle(frame,
                      pt1,
                      pt2,
                      (0,0,255),
                      3)

    # show the frame
    cv2.imshow('frame', frame)

    if cv2.waitKey(3) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()



