'''
This is for error handling when the bee image is outside the background image.
'''

def bee_corner_correction(bee_img, pos_x, pos_y, bg_h, bg_w, bee_h, bee_w):
    ### check pos_x and pos_y within range
    ### RIGHT
    if pos_x + bee_w > bg_w:
        x1 = bg_w - pos_x
        bee_img = bee_img[0:bee_h,0:x1]

    #### LEFT
    if pos_x < 0:
        x2 = -1*pos_x
        bee_img = bee_img[0:bee_h, x2:bee_w]

    ### DOWN
    if pos_y + bee_h > bg_h:
        y1 = bg_h - pos_y
        bee_img = bee_img[0:y1, 0:bee_w]

    ### UP
    if pos_y  < 0:
        y2 = -1*pos_y
        bee_img = bee_img[y2:bee_h, 0:bee_w]

    return bee_img

