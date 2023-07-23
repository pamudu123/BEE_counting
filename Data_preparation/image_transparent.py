'''
This functionality is used to set up bee images transparently on the background.
'''

import cv2
import numpy as np

def image_overlay(img1, img2, location, min_thresh=0, is_transparent=False):
    h, w = img1.shape[:2]
    h1, w1 = img2.shape[:2]
    x, y = location
    roi = img1[y:y + h1, x:x + w1]

    gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, min_thresh, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)


    img_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    img_fg = cv2.bitwise_and(img2, img2, mask=mask)
    dst = cv2.add(img_bg, img_fg)
    
    # cv2.imshow("mask background",img_bg)
    # cv2.imshow("mask forground",img_fg)
    # cv2.imshow("transparent image",dst)
    # cv2.waitKey(0)

    if is_transparent:
        dst = cv2.addWeighted(img1[y:y + h1, x:x + w1], 0.1, dst, 0.9, None)
    
    # if y+h1 > h:
    img1[y:y + h1, x:x + w1] = dst

    return img1