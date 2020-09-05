# GOALS:
# 1. Show webcam
# 2. Filter ball color
# 2.a. Maybe try HSV instead of RGB
# 3. Done


import cv2
from functools import partial

cap = cv2.VideoCapture(4)

color = input("What color to threshold: ")

filters = {
    "min": [0, 0, 0], # HSV minimum values
    "max": [179, 255, 255] # HSV maximum values
}

def update_range(edge, channel, value):
    # edge = "min" or "max"
    # channel = 0, 1, 2 (H, S, V)
    # value = new slider value
    filters[edge][channel] = value

# Create sliders to filter colors from image
cv2.namedWindow("mask")

# createTrackbar(name, window name, min value, max value, function to call on change)
cv2.createTrackbar("h_min", "mask", 0, 179, partial(update_range, "min", 0))
cv2.createTrackbar("s_min", "mask", 0, 255, partial(update_range, "min", 1))
cv2.createTrackbar("v_min", "mask", 0, 255, partial(update_range, "min", 2))
cv2.createTrackbar("h_max", "mask", 0, 179, partial(update_range, "max", 0))
cv2.createTrackbar("s_max", "mask", 0, 255, partial(update_range, "max", 1))
cv2.createTrackbar("v_max", "mask", 0, 255, partial(update_range, "max", 2))

while cap.isOpened():
    # 1. OpenCV gives you a BGR image
    _, bgr = cap.read()
    cv2.imshow("bgr", bgr)

    # 2. Convert BGR to HSV where color distributions are better
    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
    cv2.imshow("hsv", hsv)

    # 3. Use filters on HSV image
    mask = cv2.inRange(hsv, tuple(filters["min"]), tuple(filters["max"]))
    cv2.imshow("mask", mask)

    key = cv2.waitKey(10)
    if key & 0xFF == ord("q"):
        break

cap.release()
