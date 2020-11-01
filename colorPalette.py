import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, a window
img = cv2.imread("appletree.jpeg")
#np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('Rl','image',0,255,nothing)
cv2.createTrackbar('Gl','image',0,255,nothing)
cv2.createTrackbar('Bl','image',0,255,nothing)
cv2.createTrackbar('Ru','image',0,255,nothing)
cv2.createTrackbar('Gu','image',0,255,nothing)
cv2.createTrackbar('Bu','image',0,255,nothing)

# create switch for ON/OFF functionality
# switch = '0 : OFF \n1 : ON'
# cv2.createTrackbar(switch, 'image',0,1,nothing)

while(1):
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    rl = cv2.getTrackbarPos('Rl','image')
    gl = cv2.getTrackbarPos('Gl','image')
    bl = cv2.getTrackbarPos('Bl','image')
    ru = cv2.getTrackbarPos('Ru','image')
    gu = cv2.getTrackbarPos('Gu','image')
    bu = cv2.getTrackbarPos('Bu','image')
    # print(rl)
    # print(gl)
    # print(bl)
    # print(ru)
    # print(gu)
    # print(bu)


    lower = np.array([bl, gl, rl], dtype = "uint8")
    upper = np.array([bu, gu, ru], dtype = "uint8")
    print(lower)
    print(upper)
    mask = cv2.inRange(img, lower, upper)
    output = cv2.bitwise_and(img, img, mask = mask)

    cv2.imshow('image', np.hstack([img, output]))


    # s = cv2.getTrackbarPos(switch,'image')

    # if s == 0:
    #     img[:] = 0
    # else:
    #     img[:] = [b,g,r]

cv2.destroyAllWindows()