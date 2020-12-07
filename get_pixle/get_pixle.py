
import numpy as np
import cv2

image = cv2.imread('water_coins.jpg')

# image_width_index =np.shape([[1]])
# image_height_index = np.shape([1])
#
# print(image[0, 0])
# print(image[image_height_index, image_height_index])

# redColor = (0, 0, 255)
# greenColor = (0, 255, 0)
# blueColor = (B,G,R)
# blackColor = (0, 0, 0)
# whiteColor = (255, 255, 255)

h, w, ch_numbers = np.shape(image)



for py in range(0,h):
    for px in range(0,w):
        # print('Pixel value of Pos {}:{} is {}'.format(py, px, image[py][px]))
        w_dth = 0
        h_eigth = 0
        B = 0
        G = 0
        R = 0

        while h_eigth  <=250:
            image[w_dth, h_eigth] = (B,G,R)
            # w_dth+=1
            h_eigth+=1
            B+=1
            G+=1
            R+=1






cv2.imwrite('new_image.png', image)