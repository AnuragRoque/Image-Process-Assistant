import cv2
import numpy as np
import pyautogui

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define the range of skin color in HSV
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    # extract skin color from the image
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    # find contours in the mask
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # find the contour with the largest area
    if len(contours) > 0:
        contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(contour)

        # draw a rectangle around the contour
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # move the mouse pointer to the center of the rectangle
        pyautogui.moveTo(x + w // 2, y + h // 2)

    # display the frame
    cv2.imshow('frame', frame)
    def left_click_with_finger():
        pyautogui.mouseDown(button='left')
        pyautogui.mouseUp(button='left')

    # exit if the user presses 'q'
    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()